from django.shortcuts import render
from django.conf import settings
from .models import Category


# Create your views here.
def generate_category(request, category):
    category = str(category).capitalize()
    categories = Category.objects.filter(name=category).first()
    if categories is None:
        category = str(category).lower()
        categories = Category.objects.filter(name=category).first()
    if categories is None:
        return render(request, 'Front/templates/404.html', status=404)
    context = {
        'shopName': settings.SHOP_NAME,
        'category': categories,
    }
    return render(request, 'Front/shop.html', context)
