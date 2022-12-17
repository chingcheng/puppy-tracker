from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# record = CATEGORY
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Log(models.Model):
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category,
        related_name="logs",
        on_delete=models.CASCADE
    )
