from rest_framework import serializers

from ifib.models import Films, Practice


class PracticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Practice
        fields = '__all__'
