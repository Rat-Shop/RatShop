from django.db import models


# Create your models here.
class HotPay(models.Model):
    secret = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return "Usługa HotPay"

