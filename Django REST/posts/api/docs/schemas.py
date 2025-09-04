from drf_spectacular.utils import extend_schema

from posts.api.docs.serializers import ImageUploadResponseSerializer, UnauthorizedResponseSerializer
from posts.api.serializers import ImageUploadSerializer

image_upload_doc_schema = extend_schema(
    request=ImageUploadSerializer,
    responses={
        201: ImageUploadResponseSerializer,
        401: UnauthorizedResponseSerializer,
    },
)
