from django.db import models


class EquipmentGroupEnum(models.TextChoices):
    SCINTIGRAPHY = "scintigraphy", "Сцинтиграфия"
    SINGLE_PHOTON_EMISSION_TOMOGRAPHY = "single_photon_emission_tomography", "Однофотонная эмиссионная томография"
    POSITRON_EMISSION_TOMOGRAPHY = "positron_emission_tomography", "Позитронная эмиссионная томография"
    COMPUTED_TOMOGRAPHY = "computed_tomography", "Компьютерная томография"
    MRI = "mri", "Магнитно-резонансная томография"
    RADIATION_THERAPY = "radiation_therapy", "Дистанционная лучевая терапия"
