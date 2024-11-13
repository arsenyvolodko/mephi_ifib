from django_filters import rest_framework as filters

from ifib.enums import EquipmentGroupEnum


class EquipmentFilterSet(filters.FilterSet):
    id = filters.AllValuesMultipleFilter(
        field_name="id",
    )

    equipment_group = filters.AllValuesMultipleFilter(
        field_name="equipment_group",
        choices=EquipmentGroupEnum.choices
    )

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )
