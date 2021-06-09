from django.shortcuts import render
from django.conf import settings
from categories.models import ShopCategory


# Create your views here.

def home_view(request):
    context = {
        'shopName': settings.SHOP_NAME,
        'categories': ShopCategory.objects.all(),
    }
    return render(request, 'Front/index.html', context)


