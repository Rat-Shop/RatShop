# Generated by Django 3.2.4 on 2021-06-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_payment_hotpay'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_psc',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='sale_price_psc',
            field=models.FloatField(blank=True, null=True),
        ),
    ]