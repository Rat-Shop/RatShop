from django.shortcuts import render
from .models import Item
from django.conf import settings
from Front.sidebar import sidebar_data
from Front.sidebar import sidebar_data

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
    s_d = sidebar_data()
    context = {
        'sidebarSum': s_d[0],
        'sidebarData': s_d[1],
        'shopName': settings.SHOP_NAME,
        'item': found_item,
        'price': price,
    }
    return render(request, 'Front/produkt.html', context)


# Payment processor

def process_payment(request):
    if request.method == "POST":
        if request.POST.get('nick'):
            nick = request.POST['nick']
        else:
            return render(request, 'Front/templates/404.html', status=404)
        if request.POST.get('email'):
            email = request.POST['email']
        else:
            return render(request, 'Front/templates/404.html', status=404)
        if request.POST.get('itemID'):
            item_id = request.POST['itemID']
            found_item = Item.objects.filter(id=item_id).first()
            if found_item.sale:
                price = found_item.sale_price
            else:
                price = found_item.price
        else:
            return render(request, 'Front/templates/404.html', status=404)
        if request.POST["metoda"] == "Przelew":
            s_d = sidebar_data()
            context = {
                'sidebarSum': s_d[0],
                'sidebarData': s_d[1],
                'price': price,
                'ID': item_id,
                'email': email,
                'nickname': nick,
            }
            return render(request, "Front/Payments/Przelew_redirect.html", context)
        elif request.POST["metoda"] == "":
            pass
        else:
            return render(request, 'Front/templates/404.html', status=404)
    else:
        return render(request, 'Front/templates/404.html', status=404)
