from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_cart/$', views.add_cart, name='add_cart'),
	url(r'^(?P<products_id>[0-9]+)/add/$', views.setting_products, name='add_product'),
	url(r'^(?P<personproducts_id>[0-9]+)/renew/$', views.renew_product, name='renew_product'),
	url(r'^check_buy/$', views.check_buy, name='check_buy'),
	#url(r'^view_cart/$', views.view_cart, name='view_cart'),
	#url(r'^clean_cart/$', views.clean_cart, name='clean_cart'),
]