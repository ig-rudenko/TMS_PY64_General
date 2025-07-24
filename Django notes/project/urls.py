"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from notes.views import home, register, create_note_view, note_view, notes_list_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),

    path("notes", notes_list_view, name="note-list"),
    path("notes/create", create_note_view, name="create-note"),
    path("notes/<int:note_id>", note_view, name="note-view"),
]
