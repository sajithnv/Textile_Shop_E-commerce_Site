# Generated by Django 3.2 on 2021-04-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210427_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_cart',
            name='item_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]