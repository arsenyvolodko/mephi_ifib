from django.urls import path

from ifib.api.nuclear_medicine_intro.equipment.views import ListEquipmentView

urlpatterns = [
    path("equipment/", ListEquipmentView.as_view()),
]
