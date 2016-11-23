"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import hosts.urls 
import accounts.urls
import blog.urls

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^hosts/',include(hosts.urls)),
	url(r'^accounts/',include(accounts.urls)),
	url(r'^blog/',include(blog.urls)),
	url(r'^$', 'commoni.views.index', name='home_index'),
	url(r'^about_us/', 'commoni.views.about_us', name='about_me'),
	#url(r'^tos/', 'commoni.views.tos', name='tos'),
	#url(r'^tickets/', include('simpleticket.urls')),
]
