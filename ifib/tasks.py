from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_verification_email(email: str, code: str):
    subject = "Код подтверждения регистрации"
    message = f"Ваш код подтверждения: {code}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
