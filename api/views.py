from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .serializers import UserSignUpSerializer

User = get_user_model()


@api_view(["GET"])
def health(request: Request) -> Response:  # noqa: ARG001
    """Simple health-check endpoint."""
    return Response({"status": "ok"})


@api_view(["GET"])
def version(request: Request) -> Response:  # noqa: ARG001
    """Return a simple version payload for the backend."""
    return Response({"name": "cv-match-backend", "version": "0.1.0"})


@extend_schema(request=UserSignUpSerializer, responses=UserSignUpSerializer)
@api_view(["POST"])
def sign_up(request: Request) -> Response:
    """Sign up a new user."""
    serializer = UserSignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    user = User.objects.create_user(
        username=data["email"],
        email=data["email"],
        password=data["password"],
    )

    return Response({"status": "ok", "user_id": user.id})


