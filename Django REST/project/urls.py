"""
URL configuration for DjangoProjectPosts project.

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

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from posts.views import PostsListView

urlpatterns = [
    path("", PostsListView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("accounting/", include("accounting.urls")),
    path("posts/", include("posts.urls")),
    path("api/v1/", include("posts.api.urls", namespace="api")),
    path("api/auth/token/login", TokenCreateView.as_view(), name="token-create"),
    path("api/auth/token/logout", TokenDestroyView.as_view(), name="token-destroy"),
    path("api/token/", TokenObtainPairView.as_view(), name="jwt-obtain-pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
