# Generated by Django 3.2.4 on 2021-06-30 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotPay', '0004_delete_hotpaypayment'),
        ('item', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='HotPay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='HotPay.hotpay'),
        ),
    ]
