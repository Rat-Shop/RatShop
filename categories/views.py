from django.shortcuts import render
from django.conf import settings
from .models import ShopCategory
from item.models import Item
from Front.sidebar import sidebar_data


# Create your views here.
def generate_category(request, category):
    category = str(category).capitalize()
    categories = ShopCategory.objects.filter(name=category).first()
    if categories is None:
        category = str(category).lower()
        categories = ShopCategory.objects.filter(name=category).first()
    if categories is None:
        return render(request, 'Front/templates/404.html', status=404)
    items = Item.objects.filter(shop=categories).all()
    s_d = sidebar_data()
    context = {
        'sidebarSum': s_d[0],
        'sidebarData': s_d[1],
        'shopName': settings.SHOP_NAME,
        'category': categories,
        'items': items,
    }
    return render(request, 'Front/shop.html', context)
