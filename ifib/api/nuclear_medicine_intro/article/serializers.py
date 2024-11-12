from rest_framework import serializers

from ifib.api.serializers import BasePaginationSerializer
from ifib.models import Article


class ArticlesRequestSerializer(serializers.Serializer):
    search_name = serializers.CharField(required=False, allow_blank=True, default="")
    page_size = serializers.IntegerField(min_value=1, default=5)
    page_number = serializers.IntegerField(min_value=1, default=1)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"

    def to_representation(self, instance: Article):
        representation = super().to_representation(instance)
        representation["coverUrl"] = representation.pop("cover")
        representation["documentUrl"] = representation.pop("document")
        return representation


class BriefArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["id", "name", "author", "cover"]

    def to_representation(self, instance: Article):
        representation = super().to_representation(instance)
        representation["coverUrl"] = representation.pop("cover")
        return representation


class BriefArticleSerializerResponse(BasePaginationSerializer):
    items = BriefArticleSerializer(many=True)
