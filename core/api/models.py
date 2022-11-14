from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
    color = models.CharField(max_length=7, null=True, default="#4076ff")

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(blank=True)
    category = models.ManyToManyField(Category, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} | {self.user.username}"

class Event(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.user.username}"