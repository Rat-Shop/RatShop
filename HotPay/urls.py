from django.urls import path
from .views import payment_redirect_przelew, returned, payment_redirect_psc

urlpatterns = [
    path('HotPay/platnosc/przelew/', payment_redirect_przelew),
    path('HotPay/platnosc/psc/', payment_redirect_psc),
    path('zwrotka_hotpay', returned)
]
