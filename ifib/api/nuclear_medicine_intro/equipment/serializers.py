from rest_framework import serializers

from ifib.models import Films, Equipment


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'
