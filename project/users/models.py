import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.contrib.admin.models import LogEntry
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def normalize_email(self, email):
        return email.lower()

    def _create_user(self, email, password, is_active, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)

        user = User(email=email, is_active=is_active, is_staff=is_staff,
                    is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user_no_active(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, False, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)


class User(AbstractUser):
    username = None
    # changes email to unique and blank to false
    email = models.EmailField(unique=True, verbose_name='Email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    objects = CustomUserManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(
        max_length=50, null=True, verbose_name='Фамилия',)
    first_name = models.CharField(
        max_length=50, null=True, verbose_name='Имя',)
    middle_name = models.CharField(
        max_length=50, null=True, verbose_name='Отчество',)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_last_first_name(self):
        return "{0} {1}".format(self.last_name, self.first_name)


class UserGroup(Group):
    # только для админки

    class Meta:
        proxy = True
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class UserLog(LogEntry):
    # только для админки

    class Meta:
        proxy = True
        verbose_name = 'Действие'
        verbose_name_plural = 'История действий'
