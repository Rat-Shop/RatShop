from django.contrib import admin
from .models import HotPay, HotPayPayment

# Register your models here.
admin.site.register(HotPay)
admin.site.register(HotPayPayment)
