from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from ifib.api.nuclear_medicine_intro.equipment.serializers import (
    ListEquipmentSerializer,
    DetailEquipmentSerializer,
    GetEquipmentGroupRequestSerializer,
)
from ifib.core.pagination import PageNumberPagination
from ifib.enums.equipment_group_enum import EquipmentGroupEnum
from ifib.models import Equipment, EquipmentGroup


@api_view(["GET"])
def get_equipment_group(request: Request):
    serializer = GetEquipmentGroupRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    equipment_group_enum_obj = EquipmentGroupEnum.from_api_name(data["name"])
    equipment_group = equipment_group_enum_obj.to_db_obj()
    return Response({"id": equipment_group.id})


class ListEquipmentView(GenericAPIView, mixins.ListModelMixin):
    queryset = Equipment.objects.all()
    pagination_class = PageNumberPagination

    list_serializer_class = ListEquipmentSerializer
    detail_serializer_class = DetailEquipmentSerializer

    def filter_queryset(self, queryset: QuerySet[Equipment]) -> QuerySet[Equipment]:
        equipment_group = get_object_or_404(
            EquipmentGroup, id=self.kwargs.get("equipment_group_id")
        )
        return queryset.filter(equipment_group=equipment_group)

    def get_queryset(self) -> QuerySet[Equipment]:
        return self.filter_queryset(self.queryset).order_by("id")

    def get_serializer_class(self):
        if self.kwargs.get("equipment_id"):
            return self.detail_serializer_class
        return self.list_serializer_class

    def get(
        self, request: Request, equipment_group_id: int, equipment_id: int = None
    ) -> Response:
        get_object_or_404(EquipmentGroup, id=equipment_group_id)
        if equipment_id:
            equipment = get_object_or_404(Equipment, id=equipment_id)
            return Response(self.get_serializer_class()(equipment).data)
        else:
            return self.list(request)
