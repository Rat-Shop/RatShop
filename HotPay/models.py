from django.db import models


# Create your models here.
class HotPay(models.Model):
    secret = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hash = models.CharField(max_length=255, default="sha256")

    def __str__(self):
        return "Usługa HotPay"


class HotPayPayment(models.Model):
    HotPay = models.ForeignKey(HotPay, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, default=0.00, null=True)
    order_id = models.IntegerField()
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(default=2)

    def __str__(self):
        return 'ID płatności: ' + str(self.payment_id)
