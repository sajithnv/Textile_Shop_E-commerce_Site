from django.conf.urls import url
from account.views import signup
from django.contrib.auth import views as auth_views

urlpatterns=[
	url(r'^signup/$',signup,name='signup1'),
	url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login1'),
	url(r'^logout/$',auth_views.LogoutView.as_view(next_page='stock1:index1'),name='logout1'),
]