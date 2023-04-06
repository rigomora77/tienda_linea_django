# Generated by Django 4.1.7 on 2023-04-06 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo_codes', '0001_initial'),
        ('orders', '0003_order_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promo_codes.promocode'),
        ),
    ]
