# Generated by Django 3.2 on 2021-04-30 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_rename_model_purchase_model_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_my_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=200, null=True)),
                ('item_id', models.PositiveIntegerField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('bill_addrs', models.TextField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('unit_price', models.FloatField(blank=True, null=True)),
                ('img', models.CharField(blank=True, max_length=2000, null=True)),
                ('item_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='model_purchase_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=200, null=True)),
                ('grand_total', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
