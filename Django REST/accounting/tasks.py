from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


def get_user(user_id) -> User | None:
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        print(f"User ID: {user_id} does not exist")
        return None

    if not hasattr(user, "email") or not getattr(user, "email"):
        print(f"User ID: {user_id} does not have an email address. Skipping email send.")
        return None

    return user


@shared_task(queue="email", rate_limit="100/m", ignore_result=True)
def simple_send_mail(user_id: int, subject: str, message: str):
    user = get_user(user_id)
    if not user:
        return

    send_mail(subject, message, settings.EMAIL_HOST_USER, [getattr(user, "email")], fail_silently=True)


@shared_task(
    queue="email", rate_limit="100/m", autoretry_for=(ValueError,), max_retries=3, ignore_result=True
)
def send_ads_email(user_id: int):
    user = get_user(user_id)
    if not user:
        return

    subject = "Your ads"
    message = "Here are your ads:\n"

    print("Sending email to", user.email)

    # TODO: Не надо раскомментировать
    # send_mail(subject, message, settings.EMAIL_ADS_HOST_USER, [getattr(user, "email")], fail_silently=True)


@shared_task
def send_ads():
    qs = User.objects.all()
    users_count = qs.count()
    limit = 100
    page = 0
    while users_count > page * limit:
        for user in qs[page : page + limit]:
            send_ads_email.delay(user.id)
        page += 1

    return {"users_count": users_count}
