# Generated by Django 3.2.4 on 2021-06-30 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HotPay', '0004_delete_hotpaypayment'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=255)),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(default=2)),
                ('HotPay', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HotPay.hotpay')),
            ],
        ),
    ]
