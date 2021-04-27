# Generated by Django 3.2 on 2021-04-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'MENS- Formal_Wear'), ('2', 'MENS- Casual_Wear'), ('3', 'MENS- Innerwear & Sleepwear'), ('4', 'MENS- IndianFestiv_wear'), ('5', 'WOMENS- Formal_Wear'), ('6', 'WOMENS- Casual_Wear'), ('7', 'WOMENS- Innerwear & Sleepwear'), ('8', 'WOMENS- IndianFestiv_wear'), ('9', 'KIDS- Casual_Wear'), ('10', 'KIDS- Innerwear & Sleepwear'), ('11', 'KIDS- IndianFestiv_wear'), ('12', 'Towels'), ('13', 'Curtains'), ('14', 'Bed_sheets')], default='1', max_length=200, verbose_name='Category')),
                ('name', models.CharField(max_length=100, verbose_name='Item_Name')),
                ('part', models.CharField(max_length=100, null=True, verbose_name='Section')),
                ('brand', models.CharField(max_length=100, null=True, verbose_name='Item_Brand')),
                ('size', models.CharField(choices=[('1', 'S'), ('2', 'M'), ('3', 'L'), ('4', 'XL'), ('5', 'XXL'), ('6', 'XXXL')], default='1', max_length=100, verbose_name='Item_Size')),
                ('stock', models.PositiveIntegerField(verbose_name='Stock')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('img', models.CharField(max_length=2000, verbose_name='Image')),
            ],
        ),
    ]