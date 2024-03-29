from django.shortcuts import render,redirect,get_object_or_404
from stock.models import model_stock,model_qty,model_customer,model_cart,model_my_orders,model_purchase_data,model_delivery_data
from stock.forms import form_stock,form_qty,form_customer,form_cart,form_my_orders,form_purchase_data
from django.contrib.auth.decorators import login_required
from django.db.models import Q #Max

def index(request):
	return render(request,'index.html')
def cart_qty(request):
	my_cart_name = request.user.username
	cart_qty123=model_cart.objects.values_list('item_id').filter(user=my_cart_name).count()
	return render(request,'nav.html',{'cart':cart_qty123})
@login_required	
def view(request,pk):
	t1=model_stock.objects.all()
	t2=model_stock.objects.filter(category=1)
	t3=model_stock.objects.filter(category=2)
	t4=model_stock.objects.filter(category=4)
	t5=model_stock.objects.filter(category=3)
	t6=model_stock.objects.filter(brand='ALLEN SOLLY')
	t7=model_stock.objects.filter(brand='LOUIS PHILIPPE')
	t8=model_stock.objects.filter(brand='PETER ENGLAND')
	t9=model_stock.objects.filter(brand='RAYMOND')
	# t10=model_stock.objects.filter(category__in=[1,2,3,4])
	t10=model_stock.objects.filter(Q(category=1)|Q(category=2)|Q(category=4)|Q(category=3))
	t11=model_stock.objects.filter(category__in=[5,6,7,8])
	t12=model_stock.objects.filter(category=5)
	t13=model_stock.objects.filter(category=6)
	t14=model_stock.objects.filter(category=7)
	t15=model_stock.objects.filter(category=8)
	t16=model_stock.objects.filter(category__in=[9,10,11])
	t17=model_stock.objects.filter(category=9)
	t18=model_stock.objects.filter(category=10)
	t19=model_stock.objects.filter(category=11)
	t20=model_stock.objects.filter(category=12)
	t21=model_stock.objects.filter(category=13)
	t22=model_stock.objects.filter(category=14)
	t23=model_stock.objects.filter(category__in=[12,13,14])
	t24=model_stock.objects.filter(part='GIRL')
	t25=model_stock.objects.filter(part='BOY')
	t26=model_stock.objects.filter(part='NEW_BORN')

	if pk=='1':
		return render(request,'m_formal.html',{'cate1':t2})	
	elif pk=='2':
		return render(request,'m_casual.html',{'cate2':t3})		
	elif pk=='3':
		return render(request,'m_sleep.html',{'cate3':t5})
	elif pk=='4':
		return render(request,'m_festive.html',{'cate4':t4})
	elif pk=='5':
		return render(request,'allen_solly.html',{'cate5':t6})	
	elif pk=='6':
		return render(request,'louis_philippe.html',{'cate6':t7})	
	elif pk=='7':
		return render(request,'peter_england.html',{'cate7':t8})
	elif pk=='8':
		return render(request,'raymond.html',{'cate8':t9})	
	elif pk=='9':
		return render(request,'all_men.html',{'cate9':t10})
	elif pk=='10':
		return render(request,'all_women.html',{'cate10':t11})	
	elif pk=='11':
		return render(request,'w_formal.html',{'cate11':t12})	
	elif pk=='12':
		return render(request,'w_casual.html',{'cate12':t13})	
	elif pk=='13':
		return render(request,'w_sleep.html',{'cate13':t14})	
	elif pk=='14':
		return render(request,'w_festive.html',{'cate14':t15})	
	elif pk=='15':
		return render(request,'all_kids.html',{'cate15':t16})
	elif pk=='16':
		return render(request,'k_casual.html',{'cate16':t17})
	elif pk=='17':
		return render(request,'k_sleep.html',{'cate17':t18})
	elif pk=='18':
		return render(request,'k_festive.html',{'cate18':t19})	
	elif pk=='19':
		return render(request,'towels.html',{'cate19':t20})
	elif pk=='20':
		return render(request,'curtains.html',{'cate20':t21})
	elif pk=='21':
		return render(request,'bed_sheets.html',{'cate21':t22})
	elif pk=='22':
		return render(request,'others.html',{'cate22':t23})	
	elif pk=='23':
		return render(request,'girls.html',{'cate23':t24})
	elif pk=='24':
		return render(request,'boys.html',{'cate24':t25})
	elif pk=='25':
		return render(request,'new_born.html',{'cate25':t26})																	
	else:
		return render(request,'views.html',{'cate':t1})	

def selected_item(request,pk):
	uniq_data=model_stock.objects.filter(id=pk)
	data=form_qty(request.POST or None)
	if data.is_valid():
		data.save()
	return render(request,'selected_item.html',{'selected_data':uniq_data,'new_data':data})		
def register(request,pk):
	u_register=form_customer(request.POST or None)	
	if u_register.is_valid():
		u_register.save()
		return redirect('stock1:selected_item1',pk=pk)
	return render(request,'registerhtml.html',{'user_reg':u_register})	
def add_to_cart(request,pk):
		u_name=request.user.username
		price_filter=model_stock.objects.filter(id=pk)
		customer_data=model_customer.objects.values_list('user_name')
		all_data=model_customer.objects.values_list('Phone','Billing_addrs').filter(user_name=u_name)
	
		pric=0 # ITEM PRICE
		img1=''
		name=''	
		for i in price_filter:
			pric+=i.price
			img1+=i.img
			name+=i.name
		total=pric # TOTAL AMOUNT
	
		registered=0
		addrs_filter = None
		phone_filter = None	
		for i in customer_data:
			if u_name in i :
				filter1=all_data[0]
				phone_filter=filter1[0]
				addrs_filter=filter1[1]
				registered+=1	

		user_order = model_cart.objects.create(user=u_name,item_id=pk,total=total,quantity=1,bill_addrs=addrs_filter,phone=phone_filter,unit_price=total,img=img1,item_name=name)	
	return render(request,'item.html',{'registered1':registered,'price_filter1':price_filter})	
def view_cart(request):		# hashed comment for : when someone add the item into their cart then,other users can only purchase the remaining qty
	my_cart_name=request.user.username
	get_data=model_cart.objects.filter(user=my_cart_name)
	cart_total=model_cart.objects.values_list('total').filter(user=my_cart_name)
	all_cart_id=model_cart.objects.values_list('item_id').filter(user=my_cart_name)
	n=0
	someone_purchased=0
	stock_qty1=0
	total_j=0
	which_item=[] #out of stock items
	for i in all_cart_id:
		for m in i:
			cart_qty=model_cart.objects.values_list('quantity').filter(user=my_cart_name,item_id=m)#hint: remove "user=my_cart_name,"
			stock_qty=model_stock.objects.values_list('stock').filter(id=m)
			for k in stock_qty:
				stock_qty1=k[0]
			for j in cart_qty:
				for l in j:
					total_j=l
			if total_j > stock_qty1:
				which_item.append(m)
				someone_purchased+=1
	grand_total=0
	afr_discount=0
	for i in cart_total:
		for j in i:
			grand_total += j
	discount=.08*grand_total	
	afr_discount=grand_total-discount
	afr_round_amt=0
	round_amt=0
	grand_total_afr_round_amt=0
	if grand_total >= 1:
		round_amt1= afr_discount%10    #get the last digit
		grand_total_afr_round_amt += afr_discount-round_amt1
		round_amt=afr_discount-grand_total_afr_round_amt
	cart_qty123=model_cart.objects.values_list('item_id').filter(user=my_cart_name).count()
	context={
		'my_name':my_cart_name,
		'my_cart_details':get_data,
		'grand_total1':grand_total,
		'afr_discount1':afr_discount,
		'discount1':discount,
		'round_amt1':round_amt,
		'afr_round_amt1':int(grand_total_afr_round_amt),
		'someone_purchased1':someone_purchased,
		'stock_balance':stock_qty1,
		'cart_qty1':cart_qty123,
		'which_item1':which_item,
		
	}
	return render(request,'view_carthtml.html',context)

def proceed_to_buy(request,grand_total):
	my_name=request.user.username
	cart_data=model_cart.objects.filter(user=my_name)
	total = 0
	for i in cart_data:
		current_stock=0
		my_order=model_my_orders.objects.create	(user=i.user,item_id=i.item_id,quantity=i.quantity,total=i.total,bill_addrs=i.bill_addrs,phone=i.phone,unit_price=i.unit_price,img=i.img,item_name=i.item_name)
		get_stock=model_stock.objects.filter(id=i.item_id).values_list('stock')
		total += i.total
		for j in get_stock:
			current_stock+=j[0]
		new_stock=current_stock-i.quantity
		stock_minusing=model_stock.objects.filter(id=i.item_id).update(stock=new_stock)
	profit = ((total / 2 ) -(total - int(grand_total)))
	cart_data.delete()	
	my_purchase=model_purchase_data.objects.create(user=my_name,grand_total=grand_total,before_discount=total,bill_wise_profit=profit)
	return redirect('stock1:bill_page1',pk='0')
def bill_page(request,pk):
	pk1=int(pk)
	my_name=request.user.username
	purchase_data = model_purchase_data.objects.filter(user=my_name)
	date1 = ''
	grand_total = 0
	delivery_status = 0	
	if purchase_data.count() > 1:	
		selected_data = model_purchase_data.objects.filter(user=my_name).last()
		date1 += str(selected_data.date)
		grand_total += selected_data.grand_total
		delivery_status += selected_data.delivery_status
	elif purchase_data.count() == 1:		
		for i in purchase_data:
			date1 += str(i.date)
			grand_total += i.grand_total
	phone_addrs = model_customer.objects.values_list('Phone','Billing_addrs').filter(user_name=my_name)	
	phone=0
	addrs=''
	for i in phone_addrs:
		phone += i[0]
		addrs += i[1]
	content = {
		'purchase_data1':purchase_data,
		'delivery_status1':delivery_status,
		'my_name1':my_name,
		'date2':date1,
		'grand_total1':grand_total,
		'phone1':phone,
		'addrs1':addrs,
		'date12':date1,
		'pk1':pk1
	}
	return render(request,'purchased.html',content)
def contact(request):
	return render(request,'contact.html')
def helpp(request):
	return render(request,'helpp.html')	
def delete_from_cart(request,pk,qty):
	my_name=request.user.username
	data=model_cart.objects.filter(user=my_name,item_id=pk)
	unit_price=model_stock.objects.values_list('price').filter(id=pk)[0]
	tot_qty=model_stock.objects.values_list('stock').filter(id=pk)[0]
	if int(qty) > 1:
		model_cart.objects.filter(user=my_name,item_id=pk).update(quantity=int(qty)-1,total=(int(qty)-1)*unit_price[0])# qty ++ AND total update
	elif data != None:
		data.delete()
	return redirect('stock1:view_cart1')
def edit_cart(request,pk):
	my_name=request.user.username
	data=model_cart.objects.filter(user=my_name,item_id=pk)
	if data != None:
		data.delete()
	return redirect('stock1:selected_item1',pk=pk)
def edit_cart_plus(request,pk,qty):
	my_name=request.user.username
	unit_price=model_stock.objects.values_list('price').filter(id=pk)[0]
	tot_qty=model_stock.objects.values_list('stock').filter(id=pk)[0]
	
	if int(qty) <= tot_qty[0]:
		model_cart.objects.filter(user=my_name,item_id=pk).update(quantity=int(qty)+1,total=(int(qty)+1)*unit_price[0])# qty ++ AND total update
	return redirect('stock1:view_cart1')
def my_orders(request):
	my_name=request.user.username
	datas=model_my_orders.objects.filter(user=my_name)
	purchased = 0
	if datas.count() > 0:
		purchased +=1
	return render(request,'orderslist.html',{'datas1':datas,'purchased1':purchased})
def delivery(request):
	del_data=model_delivery_data.objects.all()
	del_data.delete()
	all_cust=model_customer.objects.values_list('user_name','Billing_addrs','Phone')
	all_data_count = 0		
	for i in all_cust:
		user = i[0]
		grand_totals = 0
		addrs = i[1]
		phone = i[2]
		all_data=model_purchase_data.objects.filter(user=i[0])
		for j in all_data:
			if j.delivery_status == 0:
				grand_totals += j.grand_total
		if grand_totals != 0:
			all_data_count += 1
			zz= model_delivery_data.objects.create(user=user,grand_total_all=grand_totals,bill_addrs=addrs,phone=phone)
	all_data=model_delivery_data.objects.all()
	return render(request,'delivery_boy.html',{'all_data1':all_data,'count1':all_data_count})
def delivered(request,pk):
	cust_name=model_delivery_data.objects.values_list('user').filter(id=pk)
	name = ''
	for i in cust_name:
		name += i[0]
	a =	model_purchase_data.objects.filter(user=name).update(delivery_status=1)
	b =	model_my_orders.objects.filter(user=name).update(delivery_status=1)
	return redirect('stock1:delivery1')
def transactions(request):
	all_purchase_data =	model_purchase_data.objects.all()
	grand_total = 0
	total_profit = 0
	all_data=model_purchase_data.objects.values_list('grand_total','bill_wise_profit')
	for j in all_data:
		grand_total += j[0]
		total_profit += j[1]
	pending_balance = 0	
	pending_profit = 0
	data = model_purchase_data.objects.values_list('grand_total','bill_wise_profit').filter(delivery_status=0)
	for j in data:
		pending_balance += j[0]
		pending_profit += j[1]
	total = grand_total - pending_balance
	profit = total_profit - pending_profit
	content1 = {
		'all_purchase_data1':all_purchase_data,
		'total1':total,
		'pending_balance1':pending_balance,
		'grand_total1':grand_total,
		'profit1':profit,
		'pending_profit1':pending_profit,
		'total_profit1':total_profit,
		
	}	
	return render(request,'transactions.html',content1)