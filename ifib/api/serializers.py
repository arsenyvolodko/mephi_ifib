from rest_framework import serializers


class BasePaginationSerializer(serializers.Serializer):
    total_items = serializers.IntegerField()
    page_size = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    page_number = serializers.IntegerField()
    items = serializers.Serializer()
