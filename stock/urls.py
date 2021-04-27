from django.conf.urls import url
from stock.views import index,view_cart,contact,helpp,view,selected_item,calculate,stock_minusing,paid_page,register#add

urlpatterns=[
	url(r'^$',index,name='index1'),
	# url(r'^add/$',add,name='add1'),
	url(r'^view/(?P<pk>\d+)$',view,name='view1'),
	url(r'^selected_item/(?P<pk>\d+)$',selected_item,name='selected_item1'),
	url(r'^selected/(?P<pk>\d+)$',calculate,name='calculate1'),
	url(r'^register/(?P<pk>\d+)$',register,name='register1'),
	url(r'^stock_minusing/(?P<pk>\d+)$',stock_minusing,name='stock_minusing1'),
	url(r'^stock_minusing/paid_details(?P<pk>\d+)$',paid_page,name='paid_page1'),
	url(r'^my_cart/$',view_cart,name='view_cart1'),
	url(r'^contact/$',contact,name='contact1'),
	url(r'^help/$',helpp,name='helpp1'),
]
