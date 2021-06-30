from django.db import models


# Create your models here.
class HotPay(models.Model):
    secret = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return "Usługa HotPay"


class HotPayPayment(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    HotPay = models.ForeignKey(HotPay, on_delete=models.PROTECT)
    price = models.FloatField(blank=True, default=0.00, null=True)
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(default=2)

    def __str__(self):
        return str(self.pk) + '. ID płatności: ' + str(self.payment_id)
