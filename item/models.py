from django.db import models
from categories.models import ShopCategory
from HotPay.models import HotPay


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=2137)
    image = models.CharField(max_length=256, blank=True)
    shop = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    sale = models.BooleanField(default=False)
    sale_price = models.FloatField(blank=True, null=True)
    sale_price_psc = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, default=0.00, null=True)
    price_psc = models.FloatField(blank=True, default=0.00, null=True)
    command = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Payment(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    HotPay = models.ForeignKey(HotPay, on_delete=models.PROTECT, blank=True, null=True)
    price = models.FloatField(blank=True, default=0.00, null=True)
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(default=2)

    def __str__(self):
        return str(self.pk) + '. ID płatności: ' + str(self.payment_id)
