from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'Новая'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнена'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return self.title
