# Generated by Django 5.1.1 on 2024-09-30 12:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ifib", "0003_teammember_description_alter_user_registration_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedbackForm",
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
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("text", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="registration_token",
            field=models.UUIDField(
                default=uuid.UUID("a56582db-d22b-43bb-b19e-38de707939fe"), null=True
            ),
        ),
    ]
