from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("version/", views.version, name="version"),
    path("sign-up/", views.sign_up, name="sign_up"),
]

