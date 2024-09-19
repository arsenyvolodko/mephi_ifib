from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ifib.models import User
from .serializers import (
    UserRegisterSerializer,
    ConfirmRegisterSerializer,
    UpdateConfirmationCodeRequest,
)
from .tools import generate_confirmation_code


@api_view(["POST"])
def register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    if User.objects.filter(username=data["username"]).first():
        return Response(
            {
                "error_message": "Пользователь с таким логином уже существует.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    user = User(
        username=data["username"],
        email=data["username"],
        is_active=False,
        confirmation_code=generate_confirmation_code(),
    )
    user.set_password(data["password"])
    user.save()
    return Response(
        {"token": user.registration_token, "confirmation_code": user.confirmation_code}
    )


@api_view(["POST"])
def register_confirm(request):
    serializer = ConfirmRegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    user: User = User.objects.filter(registration_token=data["register_token"]).first()

    if not user:
        return Response(
            {
                "error_message": "Введен неверный токен регистрации",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if user.confirmation_code_attempts_num >= 5:
        return Response(
            {
                "error_message": "Количество попыток ввода кода подтверждения превышено. Запросите новый код.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if user.confirmation_code != data["confirmation_code"]:
        user.confirmation_code_attempts_num += 1
        user.save()
        return Response(
            {
                "error_message": "Введен неверный код подтверждения",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    user.is_active = True
    user.confirmation_code = None
    user.registration_token = None
    user.save()
    token = Token.objects.get(user=user).key
    return Response({"token": token})


@api_view(["POST"])
def update_confirmation_code(request):

    serializer = UpdateConfirmationCodeRequest(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    token = serializer.validated_data["register_token"]
    user: User = User.objects.filter(registration_token=token).first()

    if not user:
        return Response(
            {
                "error_message": "Введен неверный токен регистрации",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if (
        user.confirmation_code_last_update
        and (timezone.now() - user.confirmation_code_last_update).seconds < 60
    ):
        return Response(
            {
                "error_message": "Попробуйте позже - обновлять код можно не более чем раз в минуту.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    user.confirmation_code = generate_confirmation_code()
    user.confirmation_code_attempts_num = 0
    user.confirmation_code_last_update = timezone.now()
    user.save()
    # todo send code
    return Response({"confirmation_code": user.confirmation_code})
