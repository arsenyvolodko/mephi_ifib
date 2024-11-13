from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.practice.filters import PracticeFilterSet
from ifib.api.practice.serializers import PracticeSerializer
from ifib.models import Practice


class ListPracticeView(GenericAPIView, ListModelMixin):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    filterset_class = PracticeFilterSet
    filter_backends = [DjangoFilterBackend]

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).order_by("id")

    def get(self, request: Request) -> Response:
        return self.list(request)
