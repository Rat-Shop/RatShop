from django.shortcuts import render
from django.conf import settings
from .models import HotPay, HotPayPayment
from item.models import Item


# Create your views here.
def payment_redirect(request):
    secret = HotPay.objects.first()
    if secret is None:
        return render(request, 'Front/templates/404.html')
    # Test
    request.method = 'POST'
    request.POST = {'price': 1.00, 'ID': 1, 'email': 'kamilszczurowski@Hotmail.com'}
    if request.method is 'POST':
        if request.POST['price']:
            price = request.POST['price']
        else:
            return render(request, 'Front/templates/404.html')
        if request.POST['ID']:
            name = Item.objects.filter(id=request.POST['ID']).first()
            name = name.name
        else:
            return render(request, 'Front/templates/404.html')
        if request.POST['email']:
            email = request.POST['email']
        else:
            return render(request, 'Front/templates/404.html')
        obj = HotPayPayment.objects.create(HotPay=HotPay.objects.first(), price=price, order_id=request.POST['ID'])
        payment_id = HotPayPayment.objects.filter(id=obj.pk).first()
    else:
        return render(request, 'Front/templates/404.html')
    context = {
        'shopName': settings.SHOP_NAME,
        'www': settings.SHOP_IP,
        'secret': secret.secret,
        'name': name,
        'price': price,
        'email': email,
        'id': payment_id.pk,
    }
    return render(request, 'Front/Payments/HotPay.html', context)


def returned(request):
    HotPayPayment.objects.create(HotPay=HotPay.objects.first(), price=2137, order_id=2137)
    return render(request, 'Front/templates/404.html', status=200)
