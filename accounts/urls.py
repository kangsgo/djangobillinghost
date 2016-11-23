from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^reg/$', views.user_reg, name='reg'),
	url(r'^signin/$', views.user_login, name='signin'),
	url(r'^signout/$', views.user_logout, name='signout'),
	url(r'^reset/$', views.change_password, name='password_reset'),
	url(r'^deposit/$', views.money_deposit, name='money_deposit'),
	url(r'^check/$', views.money_check, name='money_check'),
	url(r'^trade_check/$',views.trade_check,name='trade_check'), 
	#yibu
	url(r'^notify_url/$',views.notify_url_handler,name='notify_url_handler'), 
	#tongbu
	url(r'^return_url/$',views.return_url_handler,name='return_url_handler'),
]