from item.models import Payment


def sidebar_data():
    last_payments = Payment.objects.order_by('-pk').all()
    i = 0
    last_five = []
    for payment in last_payments:
        if i < 5:
            if payment.status == 1 or payment.status == 0:
                last_five.append(payment)
                i += 1
    sum_of_payments = 0
    for payment in last_payments:
        if payment.status == 1 or payment.status == 0:
            sum_of_payments += payment.price
    return sum_of_payments, last_five
