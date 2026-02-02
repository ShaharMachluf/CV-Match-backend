from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_GET


@require_GET
def health(request: HttpRequest) -> JsonResponse:  # noqa: ARG001
    """Simple health-check endpoint."""
    return JsonResponse({"status": "ok"})


@require_GET
def version(request: HttpRequest) -> JsonResponse:  # noqa: ARG001
    """Return a simple version payload for the backend."""
    return JsonResponse({"name": "cv-match-backend", "version": "0.1.0"})

