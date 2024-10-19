from django.urls import path

from .views import ListEquipmentView, get_equipment_group

urlpatterns = [
    path("equipment-group/", get_equipment_group),
    path("equipment-group/<int:equipment_group_id>/", ListEquipmentView.as_view()),
    path("equipment/<int:equipment_group_id>/<int:equipment_id>", ListEquipmentView.as_view()),
]
