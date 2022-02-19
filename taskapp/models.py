from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.utils.timezone import timedelta
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    def default_date():
        return timezone.now() + timedelta(days=3)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    # item = models.ManyToManyField(Item, blank=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # due_date = models.DateField(null=True, blank=True, default=default_date())
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.client.name} ({self.created_date.strftime("%d/%m/%Y")})'
