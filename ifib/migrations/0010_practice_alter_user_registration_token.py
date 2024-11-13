# Generated by Django 5.1.1 on 2024-11-13 18:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ifib", "0009_equipment_alter_user_registration_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="Practice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "practice_group",
                    models.CharField(
                        choices=[
                            ("vert", "VERT"),
                            ("ifib_virtual_trainers", "Виртуальные тренжаеры ИФИБ"),
                            ("planning_system", "Система планирования"),
                            ("ultrasound", "УЗИ"),
                            ("mri", "МРТ"),
                            ("gamma_spectrometer", "Гамма-спектрометр"),
                            ("biopac", "Biopac"),
                            ("gate", "GATE"),
                            ("monitor", "Monitor"),
                            ("lingwaves", "Lingwaves"),
                        ],
                        max_length=255,
                        unique=True,
                        verbose_name="Практикум",
                    ),
                ),
                ("link", models.URLField(verbose_name="Ссылка на stepik")),
            ],
            options={
                "verbose_name_plural": "Практикум",
            },
        ),
    ]
