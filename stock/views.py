from django.shortcuts import render,redirect,get_object_or_404
from stock.models import model_stock,model_purchase,model_customer,model_cart
from stock.forms import form_stock,form_purchase,form_customer,form_cart
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here
def index(request):
	return render(request,'index.html')
# def add(request):
# 	t1=form_stock(request.POST or None)
# 	if t1.is_valid():
# 		t1.save()
# 		return redirect(request,'stock1:index1')
# 	return render(request,'add.html',{'data':t1})	
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
	t10=model_stock.objects.filter(Q(category=1)|Q(category=2)|Q(category=4)|Q(category=5))
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
	data=form_purchase(request.POST or None)
	if data.is_valid():
		data.save()
	return render(request,'selected_item.html',{'selected_data':uniq_data,'new_data':data})		
def register(request,pk):
	u_register=form_customer(request.POST or None)	
	if u_register.is_valid():
		u_register.save()
		return redirect('stock1:selected_item1',pk=pk)
	return render(request,'registerhtml.html',{'user_reg':u_register})	
def calculate(request,pk):
	u_name=request.user.username
	qty_filter=model_purchase.objects.last()
	qty_list_count=model_purchase.objects.count()
	price_filter=model_stock.objects.filter(id=pk)
	customer_data=model_customer.objects.values_list('user_name')
	all_data=model_customer.objects.values_list('Phone','Billing_addrs').filter(user_name=u_name)
	
	if qty_list_count>1 :
		for i in range(qty_list_count-1):
			model_purchase.objects.first().delete()# delete unwanted data from purchase

	qty=0 # REQUESTED QUANTITY
	if qty_filter!=None:
		qty+=qty_filter.quantity
	pric=0 # ITEM PRICE
	for i in price_filter:
		pric+=i.price	
	total=qty*pric # TOTAL AMOUNT

	max_qty=0
	unit_price1=0
	img1=''
	for i in price_filter:
		max_qty+=i.stock
		unit_price1+=i.price
		img1+=i.img
	max_total=max_qty*pric

	
	registered=0
	addrs_filter = None
	phone_filter = None	
	for i in customer_data:
		if u_name in i :
			filter1=all_data[0]
			phone_filter=filter1[0]		
			addrs_filter=filter1[1]
			registered+=1	


	cart_qty_of_uniq_item=None
	t=qty
	stored=0
	qty_balance=0
	if registered==0:
		pass	
	elif total!=0.0 and total<=max_total: #we don't wan't to store unwanted datas
		cart_qty_of_uniq_item = model_cart.objects.values_list('quantity').filter(user=u_name,item_id=pk)
		queryset_filter=cart_qty_of_uniq_item
		t1=0
		if queryset_filter.count() != 0 :
			for i in cart_qty_of_uniq_item: # qty balancing, stock qty >= cart qty
				t+=i[0]  
				t1+=i[0]
			qty_balance = max_qty-t1
		if t <= max_qty and queryset_filter.count() == 0:
			user_order = model_cart.objects.create(user=u_name,item_id=pk,total=total,quantity=qty,bill_addrs=addrs_filter,phone=phone_filter,unit_price=unit_price1,img=img1)	
			stored+=1	
		elif t <= max_qty :
			current_total = model_cart.objects.values_list('total').filter(user=u_name,item_id=pk)
			current_total1=0
			for i in current_total:
				current_total1+=i[0]
			current_qty1= t1
			update_total=current_total1+total
			update_qty=current_qty1+qty
			user_order= model_cart.objects.filter(user=u_name,item_id=pk).update(total=update_total,quantity=update_qty)
			stored+=1	


	if qty_filter!= None:
		qty_filter.delete()	
	return render(request,'item.html',{'qty_balance1':qty_balance,'stored1':stored,'test_cust2':addrs_filter,'test_cust1':phone_filter,'price_filter1':price_filter,'qty_filter1':qty_filter,'total_price':float(total),'registered1':registered})	
def view_cart(request):		# hashed comment for : when someone add the item into their cart then,other users can only purchase the remaining qty
	my_cart_name=request.user.username
	get_data=model_cart.objects.filter(user=my_cart_name)
	cart_total=model_cart.objects.values_list('total').filter(user=my_cart_name)
	all_cart_id=model_cart.objects.values_list('item_id').filter(user=my_cart_name)

	n=0
	someone_purchased=0
	stock_qty1=0
	total_j=0

	for i in all_cart_id:
		for m in i:
			cart_qty=model_cart.objects.values_list('quantity').filter(user=my_cart_name,item_id=m)#hint: remove "user=my_cart_name,"
			stock_qty=model_stock.objects.values_list('stock').filter(id=m)
			for k in stock_qty:
				stock_qty1+=k[0]
			for j in cart_qty:
				for l in j:
					total_j+=l
			if total_j > stock_qty1:
				someone_purchased+=1
	
	grand_total=0
	afr_discount=0
	for i in cart_total:
		for j in i:
			grand_total += j
	discount=.1*grand_total	
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
		'cart_qty1':cart_qty123
	}
	return render(request,'view_carthtml.html',context)
# def cart_qty_info(request):
# 	my_cart_name=request.user.username
# 	cart_qty123=model_cart.objects.values_list('item_id').filter(user=my_cart_name).count()
# 	return render('main.html',{'cart_qty1':cart_qty123})
def stock_minusing(request,pk):
	stocks=model_stock.objects.filter(id=pk)#.values_list('stock',flat=True)
	qty_filter=model_purchase.objects.last()
	a=stocks
	zz=a[0].stock
	stock_balance=zz - qty_filter.quantity # a[0]=Total quantity and qty_filter.quantity= requsted qty
	stk=model_stock.objects.filter(id=pk).update(stock=stock_balance)# Total quantity
	# stk=stock_balance
	
	if stk != None:
		return redirect('stock1:paid_page1',pk=pk)
	return render(request,'item.html',{'a':zz,'qty':qty_filter.quantity,'stock_balance1':stock_balance})
def paid_page(request,pk):
	qty_filter=model_purchase.objects.last()
	price_filter=model_stock.objects.filter(id=pk)
	qty=0 # REQUESTED QUANTITY
	if qty_filter!=None:
		qty+=qty_filter.quantity
	pric=0 # ITEM PRICE
	for i in price_filter:
		pric+=i.price	
	total=qty*pric # TOTAL AMOUNT
	reg_no=str(qty_filter.reg_phone) # given number	
	billing_address=model_customer.objects.values_list('Billing_addrs',flat=True).filter(Phone=reg_no)
	az=billing_address
	for i in az:
		address=str(i)
	if qty_filter != None:	
		qty_filter.delete()	
	return render(request,'paid.html',{'adrs':address,'price_filter1':price_filter,'qty_filter1':qty_filter,'reg_no1':reg_no,'total_price':float(total)})
def contact(request):
	return render(request,'contact.html')
def helpp(request):
	return render(request,'helpp.html')	