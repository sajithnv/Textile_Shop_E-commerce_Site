from django.contrib import admin
from stock.models import model_stock,model_qty,model_customer,model_cart
# Register your models here.
class adminview(admin.ModelAdmin):
	list_display=['category','name','part','brand','size','stock','price','img']
class adminview1(admin.ModelAdmin):
	list_display=['quantity']
class adminview2(admin.ModelAdmin):
	list_display=['user_name','Billing_addrs','Phone']
class adminview3(admin.ModelAdmin):
	list_display=['user','item_id','total','quantity','bill_addrs','phone']

admin.site.register(model_stock,adminview)
admin.site.register(model_qty,adminview1)
admin.site.register(model_customer,adminview2)
admin.site.register(model_cart,adminview3)

