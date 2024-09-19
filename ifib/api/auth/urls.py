from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import register, register_confirm, update_confirmation_code

urlpatterns = [
    path("auth/register", register),
    path("auth/register/confirm", register_confirm),
    path("auth/update-confirmation-code", update_confirmation_code),
    path("auth/login", obtain_auth_token),
]
