from rest_framework import serializers

from ifib.enums.equipment_group_enum import EquipmentGroupEnum
from ifib.models import Equipment


class GetEquipmentGroupRequestSerializer(serializers.Serializer):
    name = serializers.ChoiceField(choices=EquipmentGroupEnum.api_choices())


class ListEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ("name", "cover")


class DetailEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ("name", "description", "model")
