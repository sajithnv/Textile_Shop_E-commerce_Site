from django import forms
from stock.models import model_stock,model_qty,model_customer,model_cart,model_my_orders,model_purchase_data

class form_stock(forms.ModelForm):
	class Meta:
		model = model_stock
		fields = '__all__'
		# fields=['category','name','size','quantity','price','img']
class form_qty(forms.ModelForm):
	class Meta:
		model = model_qty
		fields = ['quantity'] 		
class form_customer(forms.ModelForm):
	user_name = forms.CharField(initial='It must be log_in UserName')
	class Meta:
		model = model_customer
		fields = '__all__'
		widgets = {
			'Billing_addrs':forms.Textarea(attrs = {
				'style':'height:150px;'
				}),
		}
class form_cart(forms.ModelForm):
	class Meta:
		model = model_cart
		fields = '__all__' 	
class form_my_orders(forms.ModelForm):
	class Meta:
		model = model_my_orders
		fields = '__all__' 
class form_purchase_data(forms.ModelForm):
	class Meta:
		model = model_purchase_data
		fields = '__all__' 							