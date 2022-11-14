from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class Account(AbstractUser):
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email