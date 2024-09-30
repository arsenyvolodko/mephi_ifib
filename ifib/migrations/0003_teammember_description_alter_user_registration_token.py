# Generated by Django 5.1.1 on 2024-09-29 21:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ifib", "0002_article_alter_user_registration_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="teammember",
            name="description",
            field=models.CharField(
                default="", max_length=255, verbose_name="Должность"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="registration_token",
            field=models.UUIDField(
                default=uuid.UUID("48668949-f742-49a4-bf08-96914c0110b1"), null=True
            ),
        ),
    ]