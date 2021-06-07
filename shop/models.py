from django.db import models
from categories.models import Category


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=2137)
    image = models.CharField(max_length=256, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
