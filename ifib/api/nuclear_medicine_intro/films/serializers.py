from rest_framework import serializers

from ifib.models import Films


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Films
        fields = '__all__'
