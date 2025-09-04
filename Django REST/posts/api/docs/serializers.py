from rest_framework import serializers


class ImageUploadResponseSerializer(serializers.Serializer):
    image_path = serializers.CharField()


class JWTErrorMessageSerializer(serializers.Serializer):
    token_class = serializers.CharField(default="AccessToken")
    token_type = serializers.CharField(default="access")
    message = serializers.CharField(default="Token has wrong type")


class UnauthorizedResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(label="Учетные данные не были предоставлены.", required=True)
    code = serializers.CharField(default="token_not_valid", required=False)
    messages = serializers.ListField(child=JWTErrorMessageSerializer(), required=False)
