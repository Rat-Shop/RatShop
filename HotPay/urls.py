from django.urls import path
from .views import payment_redirect, returned

urlpatterns = [
    path('HotPay/platnosc/', payment_redirect),
    path('zwrotka_hotpay/', returned)
]
