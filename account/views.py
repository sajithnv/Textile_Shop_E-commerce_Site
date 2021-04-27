from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

# Create your views here.
def signup(request):
	t1=UserCreationForm(request.POST or None)
	if t1.is_valid():
		t1.save()
		u=t1.cleaned_data.get('username')
		p=t1.cleaned_data.get('password1')
		user=authenticate(username=u,password=p)
		login(request,user)
		return redirect('stock1:index1')
	return render(request,'signup.html',{'form':t1})
