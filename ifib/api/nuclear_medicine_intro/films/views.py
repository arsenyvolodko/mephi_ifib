from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.nuclear_medicine_intro.films.filters import FilmsFilterSet
from ifib.api.nuclear_medicine_intro.films.serializers import FilmSerializer
from ifib.models import Films


class ListFilmView(GenericAPIView, ListModelMixin):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer
    filterset_class = FilmsFilterSet
    filter_backends = [DjangoFilterBackend]

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)

    def get(self, request: Request) -> Response:
        return self.list(request)
