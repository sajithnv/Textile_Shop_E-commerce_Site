from django.conf.urls import url
from stock.views import index, edit_cart, delete_from_cart, view_cart, contact, helpp, view, selected_item, add_to_cart, proceed_to_pay, paid_page, register#add

urlpatterns=[
	url(r'^$',index,name='index1'),
	# url(r'^add/$',add,name='add1'),
	url(r'^view/(?P<pk>\d+)$',view,name='view1'),
	url(r'^selected_item/(?P<pk>\d+)$',selected_item,name='selected_item1'),
	url(r'^add_to_cart/(?P<pk>\d+)$',add_to_cart,name='add_to_cart1'),
	url(r'^register/(?P<pk>\d+)$',register,name='register1'),
	url(r'^proceed_to_pay/(?P<grand_total>\d+)$',proceed_to_pay,name='proceed_to_buy1'),
	url(r'^stock_minusing/paid_details(?P<pk>\d+)$',paid_page,name='paid_page1'),
	url(r'^my_cart/$',view_cart,name='view_cart1'),
	url(r'^contact/$',contact,name='contact1'),
	url(r'^help/$',helpp,name='helpp1'),
	url(r'^delete/(?P<pk>\d+)$',delete_from_cart,name='delete_from_cart1'),
	url(r'^edit/(?P<pk>\d+)$',edit_cart,name='edit_cart1'),
]
