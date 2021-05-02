from django.db import models

# Create your models here.

Item_category=(
		('1','MENS- Formal_Wear'),
		('2','MENS- Casual_Wear'),
		('3','MENS- Innerwear & Sleepwear'),
		('4','MENS- IndianFestiv_wear'),
		('5','WOMENS- Formal_Wear'),
		('6','WOMENS- Casual_Wear'),
		('7','WOMENS- Innerwear & Sleepwear'),
		('8','WOMENS- IndianFestiv_wear'),
		('9','KIDS- Casual_Wear'),
		('10','KIDS- Innerwear & Sleepwear'),
		('11','KIDS- IndianFestiv_wear'),
		('12','Towels'),
		('13','Curtains'),
		('14','Bed_sheets'),
	)
Item_size=(
	('1','S'),
	('2','M'),
	('3','L'),
	('4','XL'),
	('5','XXL'),
	('6','XXXL'),
	)
# Create your models here.
class model_stock(models.Model):
	category=models.CharField('Category',max_length=200,choices=Item_category,default='1')
	name=models.CharField('Item_Name',max_length=100)
	part=models.CharField('Section',max_length=100,null=True)
	brand=models.CharField('Item_Brand',max_length=100,null=True)
	size=models.CharField('Item_Size',max_length=100,choices=Item_size,default='1')
	stock=models.PositiveIntegerField('Stock')
	price=models.FloatField('Price',default=0.0)
	img=models.CharField('Image',max_length=2000)
class model_customer(models.Model):
	user_name=models.CharField('user_name',max_length=100,null=True)
	Billing_addrs=models.TextField('Billing_Address',max_length=100)
	Phone=models.IntegerField('Phone_Number')
class model_qty(models.Model):
	quantity=models.PositiveIntegerField('Quantity')
class model_cart(models.Model):
	user=models.CharField(max_length=200,null=True,blank=True)
	item_id=models.PositiveIntegerField(null=True,blank=True)
	total=models.FloatField(null=True,blank=True)
	quantity=models.PositiveIntegerField(null=True,blank=True)
	bill_addrs=models.TextField(null=True,blank=True,max_length=100)
	phone=models.IntegerField(null=True,blank=True)
	unit_price=models.FloatField(null=True,blank=True)
	img=models.CharField(max_length=2000,null=True,blank=True)
	item_name=models.CharField(max_length=100,null=True,blank=True)
class model_my_orders(models.Model):
	date=models.DateTimeField(auto_now_add=True)
	user=models.CharField(max_length=200,null=True,blank=True)
	item_id=models.PositiveIntegerField(null=True,blank=True)
	total=models.FloatField(null=True,blank=True)
	quantity=models.PositiveIntegerField(null=True,blank=True)
	bill_addrs=models.TextField(null=True,blank=True,max_length=100)
	phone=models.IntegerField(null=True,blank=True)
	unit_price=models.FloatField(null=True,blank=True)
	img=models.CharField(max_length=2000,null=True,blank=True)
	item_name=models.CharField(max_length=100,null=True,blank=True)	
	delivery_status=models.BooleanField(default=0,null=True,blank=True)
class model_purchase_data(models.Model):
	date=models.DateTimeField(auto_now_add=True)
	user=models.CharField(max_length=200,null=True,blank=True)
	grand_total=models.PositiveIntegerField(null=True,blank=True)
