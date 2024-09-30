import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from ifib.enums import RoleEnum, InterestSphereEnum, EducationalStatusEnum


class Role(models.Model):
    name = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.formatted_name) for tag in RoleEnum],
        unique=True,
    )

    def __str__(self):
        return RoleEnum(self.id).formatted_name


class User(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    birth_date = models.DateField()
    social_network = models.URLField()
    educational_status = models.CharField(choices=EducationalStatusEnum.choices(), max_length=255, blank=True, null=True)
    educational_facility = models.CharField(max_length=255, blank=True, null=True)
    sphere_of_interest = models.CharField(choices=InterestSphereEnum.choices())

    confirmation_code = models.CharField(max_length=4, blank=True, null=True)
    confirmation_code_last_update = models.DateTimeField(null=True, auto_now_add=True)
    confirmation_code_attempts_num = models.IntegerField(default=0)
    registration_token = models.UUIDField(default=uuid.uuid4(), null=True)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Роль"
    )

    class Meta:
        verbose_name_plural = "Пользователи"

    @property
    def get_role(self) -> RoleEnum | None:
        return RoleEnum(value=self.role.id) if self.role else None

    def save(self, *args, **kwargs):
        if self.get_role == RoleEnum.ADMIN:
            self.is_superuser = True
            self.is_staff = True
        super().save(*args, **kwargs)


class Article(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    author = models.CharField(max_length=255, verbose_name="Автор")
    cover = models.ImageField(upload_to="article/covers/", verbose_name="Обложка")
    document = models.FileField(
        upload_to="article/documents/", verbose_name="Документ", help_text="Формат: PDF"
    )

    class Meta:
        verbose_name_plural = "Научно-популярные статьи"

    def __str__(self):
        return f"{self.author} - {self.name}"


class TeamMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя Фамилия")
    image = models.ImageField(upload_to="team_members/", verbose_name="Фото")
    description = models.CharField(max_length=255, verbose_name="Должность")

    class Meta:
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return self.name


class FeedbackForm(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    text = models.TextField()
