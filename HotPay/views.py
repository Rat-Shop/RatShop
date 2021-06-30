import hashlib

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import HotPay, HotPayPayment
from item.models import Item
from django.views.decorators.csrf import csrf_exempt
from ServerConnection.ExecuteCommand import execute_command

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
        else:
            return render(request, 'Front/templates/404.html', status=404)
        if request.POST.get('email'):
            email = request.POST['email']
        else:
            return render(request, 'Front/templates/404.html', status=404)
        obj = HotPayPayment.objects.create(HotPay=HotPay.objects.first(), price=price, item_id=request.POST['ID'],
                                           nickname=nickname, email=email)
        if price == 0:
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
        if request.POST.get("KWOTA") and request.POST.get("ID_PLATNOSCI") and request.POST.get("ID_ZAMOWIENIA") \
                and request.POST.get("STATUS") and request.POST.get("SEKRET") and request.POST.get("HASH"):
            hash1 = "akwyNm9FcEtRb24x" + ";" + request.POST.get("KWOTA") + ";" + request.POST.get("ID_PLATNOSCI") + ";"\
                    + request.POST.get("ID_ZAMOWIENIA") + ";" + \
                    request.POST.get("STATUS") + ";" + request.POST.get("SEKRET")
            if not hashlib.sha256(hash1.encode()).hexdigest() == request.POST.get("HASH"):
                return HttpResponse(status=203)
            if request.POST["STATUS"] == "FAILURE":
                order_id = request.POST["ID_ZAMOWIENIA"]
                payment_id = request.POST["ID_PLATNOSCI"]
                HotPayPayment.objects.filter(pk=order_id).update(status=3, payment_id=payment_id)
            elif request.POST["STATUS"] == "SUCCESS":
                order_id = request.POST["ID_ZAMOWIENIA"]
                payment_id = request.POST["ID_PLATNOSCI"]
                HotPayPayment.objects.filter(pk=order_id).update(status=1, payment_id=payment_id)
                item = Item.objects.filter(pk=HotPayPayment.objects.filter(pk=order_id).first().item_id).first()
                command = item.command.replace("{name}", HotPayPayment.objects.filter(pk=order_id).first().nickname)
                rcon_result = execute_command(command)
                if rcon_result:
                    HotPayPayment.objects.filter(pk=order_id).update(status=0)
                return HttpResponse(status=200)
            return HttpResponse(status=200)
    return HttpResponse(status=203)
