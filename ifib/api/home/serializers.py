import re

from rest_framework import serializers

from ifib.models import TeamMember, FeedbackForm


class TeamMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = "__all__"

    def to_representation(self, instance: TeamMember):
        representation = super().to_representation(instance)
        representation["imageUrl"] = representation.pop("image")
        return representation


class FeedbackFormSerializer(serializers.ModelSerializer):
    allow_personal_data_processing = serializers.BooleanField(write_only=True)

    class Meta:
        model = FeedbackForm
        fields = [
            "name",
            "phone_number",
            "email",
            "text",
            "allow_personal_data_processing",
        ]

    def validate_phone_number(self, value):
        if not re.match(r"^\d{10}$", value):
            raise serializers.ValidationError("Номер телефона должен состоять из цифр.")
        return value

    def validate_allow_personal_data_processing(self, value):
        if not value:
            raise serializers.ValidationError(
                "Необходимо разрешить обработку персональных данных."
            )
        return value

    def create(self, validated_data):
        validated_data.pop("allow_personal_data_processing")
        return super().create(validated_data)
