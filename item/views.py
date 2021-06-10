from django.shortcuts import render
from .models import Item
from django.conf import settings


# Create your views here.
def generate_item(request, item_id):
    if not item_id:
        return render(request, 'Front/templates/404.html', {}, status=404)
    found_item = Item.objects.filter(id=item_id).first()
    if not found_item:
        return render(request, 'Front/templates/404.html', {}, status=404)
    if found_item.sale:
        if found_item.sale_price:
            price = str(found_item.sale_price) + ' PLN'
        else:
            price = "Darmowe"
    else:
        if found_item.price:
            price = str(found_item.price) + ' PLN'
        else:
            price = "Darmowe"
    context = {
        'shopName': settings.SHOP_NAME,
        'item': found_item,
        'price': price,
    }
    return render(request, 'Front/produkt.html', context)
