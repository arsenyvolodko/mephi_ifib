from rest_framework import serializers
from ifib.enums import EducationalStatusEnum, InterestSphereEnum


class UserRegisterSerializer(serializers.Serializer):
    last_name = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=150)
    middle_name = serializers.CharField(allow_null=True, max_length=150)
    birth_date = serializers.DateField(input_formats=["%d.%m.%Y"])
    email = serializers.EmailField()
    social_network = serializers.URLField()
    educational_status = serializers.ChoiceField(choices=EducationalStatusEnum.choices(), allow_null=True)
    educational_facility = serializers.CharField(max_length=255, required=False)
    sphere_of_interest = serializers.ChoiceField(choices=InterestSphereEnum.choices())
    password = serializers.CharField()
    password_confirmation = serializers.CharField()

    def validate(self, data):
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError(detail="Пароли не совпадают.")
        return data


class ConfirmRegisterSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField()
    register_token = serializers.UUIDField()


class UpdateConfirmationCodeRequest(serializers.Serializer):
    register_token = serializers.UUIDField()
