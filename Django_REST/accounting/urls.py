from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import register


# /accounting/

urlpatterns = [
    path("register", register, name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
