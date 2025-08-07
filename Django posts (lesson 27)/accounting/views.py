from django.shortcuts import render, redirect
from django.urls import reverse

from accounting.forms import RegisterForm
from .models import User


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            User.objects.create_user(username=username, email=email, password=password)

            return redirect(reverse("login"))

    return render(request, 'registration/register.html', {"form": form})
