# Generated by Django 3.2.4 on 2021-06-12 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotPay', '0002_alter_hotpay_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotpaypayment',
            name='payment_id',
        ),
    ]
