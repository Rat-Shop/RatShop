# Generated by Django 3.2.4 on 2021-06-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20210630_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.CharField(default='Przelew', max_length=255),
            preserve_default=False,
        ),
    ]
