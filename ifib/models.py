import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from ifib.enums import RoleEnum, InterestSphereEnum, EducationalStatusEnum, KnowledgeBaseEnum, EquipmentGroupEnum, \
    PracticeGroupEnum


class Role(models.Model):
    name = models.CharField(
        max_length=50,
        choices=RoleEnum.choices(),
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

    def save(self, *args, **kwargs):
        if RoleEnum.from_db_obj(self.role) == RoleEnum.ADMIN:
            self.is_superuser = True
            self.is_staff = True
        super().save(*args, **kwargs)


class Article(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    author = models.CharField(max_length=255, verbose_name="Автор")
    cover = models.ImageField(upload_to="nuclear_medicine_intro/article/covers/", verbose_name="Обложка")
    document = models.FileField(
        upload_to="article/documents/", verbose_name="Документ", help_text="Формат: PDF"
    )

    class Meta:
        verbose_name_plural = "Научно-популярные статьи"

    def __str__(self):
        return f"{self.author} - {self.name}"


class TeamMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя Фамилия")
    image = models.ImageField(upload_to="home/team_members/", verbose_name="Фото")
    description = models.CharField(max_length=255, verbose_name="Должность")

    class Meta:
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return self.name


class FeedbackForm(models.Model):
    name = models.CharField(max_length=255, verbose_name="Отправитель")
    phone_number = models.CharField(max_length=10, verbose_name="Номер телефона", help_text="Указан без +7")
    email = models.EmailField()
    text = models.TextField(verbose_name="Текст обращения")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    resolved = models.BooleanField(default=False, verbose_name="Обращение закрыто")

    class Meta:
        verbose_name_plural = "Обратная связь"

    def _get_resolved_emoji(self):
        return "✅" if self.resolved else "❌"

    def __str__(self):
        return f"{self._get_resolved_emoji()} {self.name} - {self.created.strftime('%d.%m.%Y %H:%M')}"


class KnowledgeBase(models.Model):
    name = models.CharField(max_length=36, choices=KnowledgeBaseEnum.choices(), unique=True, verbose_name="Название раздела")

    class Meta:
        verbose_name_plural = "База знаний"

    def __str__(self):
        return KnowledgeBaseEnum.from_db_obj(self).formatted_name


class Terms(models.Model):
    knowledge_base = models.ForeignKey(KnowledgeBase, on_delete=models.CASCADE, verbose_name="Раздел базы знаний")
    name = models.CharField(max_length=255, verbose_name="Термин")
    definition = models.TextField(verbose_name="Определение")

    class Meta:
        verbose_name_plural = "Термины"

    def __str__(self):
        return f"{self.knowledge_base} - {self.name}"


class Films(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    theme = models.CharField(max_length=255, verbose_name="Тематика/участники")
    description = models.TextField(verbose_name="Описание")
    cover = models.ImageField(upload_to="nuclear_medicine_intro/films/", verbose_name="Обложка")
    link = models.URLField(verbose_name="Ссылка на видео")

    class Meta:
        verbose_name_plural = "Видео"

    def __str__(self):
        return f"{self.name}"


class Equipment(models.Model):
    equipment_group = models.CharField(max_length=255, verbose_name="Группа оборудования", choices=EquipmentGroupEnum.choices)
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    cover = models.ImageField(upload_to="nuclear_medicine_intro/equipment/", verbose_name="Обложка/изображение модели")
    model = models.URLField(verbose_name="Ссылка на 3D-модель")

    class Meta:
        verbose_name_plural = "Оборудование"

    def __str__(self):
        return self.name


class Practice(models.Model):
    practice_group = models.CharField(max_length=255, verbose_name="Практикум", choices=PracticeGroupEnum.choices, unique=True)
    link = models.URLField(verbose_name="Ссылка на stepik")

    class Meta:
        verbose_name_plural = "Практикум"

    def __str__(self):
        return self.practice_group
