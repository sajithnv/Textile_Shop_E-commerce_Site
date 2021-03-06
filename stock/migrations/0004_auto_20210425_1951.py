# Generated by Django 3.2 on 2021-04-26 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_model_customer_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_cart',
            name='bill_addrs',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='model_cart',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='model_cart',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
