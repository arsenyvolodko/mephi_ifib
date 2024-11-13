from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.nuclear_medicine_intro.podcasts.filters import PodcastsFilterSet
from ifib.api.nuclear_medicine_intro.podcasts.serializers import PodcastSerializer
from ifib.models import Podcasts


class ListPodcastsView(GenericAPIView, ListModelMixin):
    queryset = Podcasts.objects.all()
    serializer_class = PodcastSerializer
    filterset_class = PodcastsFilterSet
    filter_backends = [DjangoFilterBackend]

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).order_by("id")

    def get(self, request: Request) -> Response:
        return self.list(request)
