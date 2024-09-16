from django.contrib.auth.models import AbstractUser
from django.db import models

from ifib.enums import RoleEnum


class Role(models.Model):
    name = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.formatted_name) for tag in RoleEnum],
        unique=True
    )

    def __str__(self):
        return RoleEnum(self.id).formatted_name


class User(AbstractUser):
    confirmation_code = models.CharField(max_length=4, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Роль')

    class Meta:
        verbose_name_plural = 'Пользователи'


class TeamMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя Фамилия")
    image = models.ImageField(upload_to='team_members/', verbose_name="Фото")

    class Meta:
        verbose_name_plural = 'Члены команды'

    def __str__(self):
        return self.name
