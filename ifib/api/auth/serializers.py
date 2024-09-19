from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password_2 = serializers.CharField()

    def validate(self, data):
        if data["password"] != data["password_2"]:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data


class ConfirmRegisterSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField()
    register_token = serializers.UUIDField()


class UpdateConfirmationCodeRequest(serializers.Serializer):
    register_token = serializers.UUIDField()
