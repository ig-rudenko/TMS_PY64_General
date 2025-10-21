from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import Token


class CustomTokenAuthentication(TokenAuthentication):
    model = Token

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if token.expires and token.expires < timezone.now():
            raise AuthenticationFailed("Token has expired")
        return user, token
