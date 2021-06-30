from django.shortcuts import render
from django.conf import settings
from categories.models import ShopCategory
from .sidebar import sidebar_data


# Create your views here.

def home_view(request):
    s_d = sidebar_data()
    context = {
        'sidebarSum': s_d[0],
        'sidebarData': s_d[1],
        'shopName': settings.SHOP_NAME,
        'categories': ShopCategory.objects.all(),
    }
    return render(request, 'Front/index.html', context)
