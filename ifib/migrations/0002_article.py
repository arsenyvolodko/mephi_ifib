# Generated by Django 5.1.1 on 2024-09-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ifib", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                ("author", models.CharField(max_length=255, verbose_name="Автор")),
                (
                    "cover",
                    models.ImageField(
                        upload_to="article/covers/", verbose_name="Обложка"
                    ),
                ),
                (
                    "document",
                    models.FileField(
                        help_text="Формат: PDF",
                        upload_to="article/documents/",
                        verbose_name="Документ",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Научно-популярные статьи",
            },
        ),
    ]