from django.db import models
from categories.models import ShopCategory


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=2137)
    image = models.CharField(max_length=256, blank=True)
    shop = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name
