# Generated by Django 3.2.4 on 2021-06-12 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('hash', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HotPayPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('payment_id', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('status', models.IntegerField(default=2)),
                ('HotPay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotPay.hotpay')),
            ],
        ),
    ]