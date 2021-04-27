from django import forms
from stock.models import model_stock,model_purchase,model_customer,model_cart

class form_stock(forms.ModelForm):
	class Meta:
		model = model_stock
		fields = '__all__'
		# fields=['category','name','size','quantity','price','img']
class form_purchase(forms.ModelForm):
	class Meta:
		model = model_purchase
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