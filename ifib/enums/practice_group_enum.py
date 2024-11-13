from django.db import models


class PracticeGroupEnum(models.TextChoices):
    VERT = "vert", "VERT"
    IFIB_VIRTUAL_TRAINERS = "ifib_virtual_trainers", "Виртуальные тренжаеры ИФИБ"
    PLANNING_SYSTEM = "planning_system", "Система планирования"
    ULTRASOUND = "ultrasound", "УЗИ"
    MRI = "mri", "МРТ"
    GAMMA_SPECTROMETER = "gamma_spectrometer", "Гамма-спектрометр"
    BIOPAC = "biopac", "Biopac"
    GATE = "gate", "GATE"
    MONITOR = "monitor", "Monitor"
    LINGWAVES = "lingwaves", "Lingwaves"
