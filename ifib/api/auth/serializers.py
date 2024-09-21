from rest_framework import serializers

from ifib.enums import InterestSphereEnum


class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    middle_name = serializers.CharField(allow_null=True, max_length=150)
    last_name = serializers.CharField(max_length=150)
    birth_date = serializers.DateField(input_formats=['%d.%m.%Y'])
    mobile_phone = serializers.CharField()
    social_network = serializers.URLField()
    grade = serializers.CharField()
    sphere_of_interest = serializers.ChoiceField(choices=InterestSphereEnum.choices())
    email = serializers.EmailField()
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
