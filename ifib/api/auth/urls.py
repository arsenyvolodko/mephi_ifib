from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import register, register_confirm, update_confirmation_code

urlpatterns = [
    path("register", register),
    path("register/confirm", register_confirm),
    path("update-confirmation-code", update_confirmation_code),
    path("login", obtain_auth_token),
]
