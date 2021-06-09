from django.db import models


# Create your models here.
class ShopCategory(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name
