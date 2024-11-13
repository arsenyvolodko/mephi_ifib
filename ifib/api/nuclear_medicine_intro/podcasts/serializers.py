from rest_framework import serializers

from ifib.models import Podcasts


class PodcastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcasts
        fields = '__all__'
