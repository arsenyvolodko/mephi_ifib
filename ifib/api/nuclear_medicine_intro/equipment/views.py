from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from ifib.api.nuclear_medicine_intro.equipment.filters import EquipmentFilterSet
from ifib.api.nuclear_medicine_intro.equipment.serializers import EquipmentSerializer
from ifib.models import Equipment


class ListEquipmentView(GenericAPIView, ListModelMixin):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filterset_class = EquipmentFilterSet
    filter_backends = [DjangoFilterBackend]

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).order_by("id")

    def get(self, request: Request) -> Response:
        return self.list(request)
