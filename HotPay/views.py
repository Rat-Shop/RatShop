from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import HotPay, HotPayPayment
from item.models import Item
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def payment_redirect(request):
    secret = HotPay.objects.first()
    if secret is None:
        return render(request, 'Front/templates/404.html')
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('nickname'):
            nickname = request.POST['nickname']
        else:
            return render(request, 'Front/templates/404.html', status=404)
        if request.POST.get('price'):
            price = request.POST['price']
        else:
            return render(request, 'Front/templates/404.html', status=404)
        if request.POST.get('ID'):
            name = Item.objects.filter(id=request.POST['ID']).first()
            name = name.name
        else:
            return render(request, 'Front/templates/404.html', status=404)
        if request.POST.get('email'):
            email = request.POST['email']
        else:
            return render(request, 'Front/templates/404.html', status=404)
        obj = HotPayPayment.objects.create(HotPay=HotPay.objects.first(), price=price, order_id=request.POST['ID'],
                                           nickname=nickname)
        if price is 0:
            return render(request, 'Front/templates/404.html', status=404)
        payment_id = HotPayPayment.objects.filter(id=obj.pk).first()
    else:
        return render(request, 'Front/templates/404.html', status=404)
    context = {
        'shopName': settings.SHOP_NAME,
        'www': settings.SHOP_IP,
        'secret': secret.secret,
        'name': name,
        'price': price,
        'email': email,
        'id': payment_id.pk,
    }
    return render(request, 'Front/Payments/HotPay.html', context, status=404)


@csrf_exempt
def returned(request):
    if request.method == "POST":
        return HttpResponse(request.POST)
    return HttpResponse('Hello world')
