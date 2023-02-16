from django.conf.urls import url
from stock.views import index, transactions, cart_qty, delivered, delivery, my_orders, edit_cart, edit_cart_plus, delete_from_cart, view_cart, contact, helpp, view, selected_item, add_to_cart, proceed_to_buy,bill_page, register

urlpatterns=[
	url(r'^$',index,name='index1'),
	url(r'^cart_qty/$',cart_qty,name='cart_qty1'),
	url(r'^view/(?P<pk>\d+)$',view,name='view1'),
	url(r'^selected_item/(?P<pk>\d+)$',selected_item,name='selected_item1'),
	url(r'^add_to_cart/(?P<pk>\d+)$',add_to_cart,name='add_to_cart1'),
	url(r'^register/(?P<pk>\d+)$',register,name='register1'),
	url(r'^my_cart/$',view_cart,name='view_cart1'),
	url(r'^contact/$',contact,name='contact1'),
	url(r'^help/$',helpp,name='helpp1'),
	# url(r'^delete/(?P<pk>\d+)$',delete_from_cart,name='delete_from_cart1'),
	url(r'^delete/(?P<pk>\d+)/(?P<qty>\d+)$',delete_from_cart,name='delete_from_cart1'),

	url(r'^edit/(?P<pk>\d+)$',edit_cart,name='edit_cart1'),
	url(r'^edit/(?P<pk>\d+)/(?P<qty>\d+)$',edit_cart_plus,name='edit_cart_plus'),


	url(r'^proceed_to_buy/(?P<grand_total>\d+)$',proceed_to_buy,name='proceed_to_buy1'),
	url(r'^bill_page/(?P<pk>\d+)$',bill_page,name='bill_page1'),
	url(r'^my_orders/$',my_orders,name='my_orders1'),
	url(r'^delivery/$',delivery,name='delivery1'),
	url(r'^delivered/(?P<pk>\d+)$',delivered,name='delivered1'),
	url(r'^transactions/$',transactions,name='transactions1'),
]
