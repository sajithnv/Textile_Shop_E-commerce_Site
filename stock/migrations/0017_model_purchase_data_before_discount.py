# Generated by Django 3.2 on 2021-05-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_remove_model_delivery_data_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_purchase_data',
            name='before_discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]