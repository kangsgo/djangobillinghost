#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from cpanelapi import client

from .models import HostProducts,Caritem,Cart
from accounts.models import UserProfile
from myhost.models import PersonHost,Personblling
import accounts.urls as accounts 

# Create your views here.
def index(request):
	prodcuts_list=HostProducts.objects.all()
	context={'prodcuts_list':prodcuts_list}
	return render(request,'index.html',context)

def add_cart(request):
	return HttpResponse("You're voting on question " )

#查看购物车
def  view_cart(request):
	if request.user.is_authenticated():
		cart_list=Caritem.objects.all()
		context={'cart_list':cart_list}
		return render_to_response('check.html',context,context_instance=RequestContext(request)) 
	else:
		return HttpResponse("妈的不存在")

#产品设置
def setting_products(request,products_id):
	if request.user.is_authenticated():
		try:
			products=HostProducts.objects.get(pk=products_id)
		except Exception as e:
			return HttpResponse(e)
		context={'products':products}
		return render(request,'buyone.html',context)
	else:
		messages.add_message(request, messages.WARNING, ' 请先登录后购买')
		return render(request,'login.html',{})

#结帐
def check_buy(request):
	if request.method == 'GET':
		return render_to_response('error.html',{'title':'发生错误','context':'非法进入'},context_instance=RequestContext(request))
	elif request.user.is_authenticated():
		id=request.user.id
		productsid=request.POST['id']
		user=User.objects.get(id=id)
		products=HostProducts.objects.get(pk=productsid)
		domain=request.POST['domain']
		paccount=request.POST['paccount']
		if PersonHost.objects.filter(domain=domain) or PersonHost.objects.filter(paccounts=paccount):
			return render(request,'error.html',{'title':'发生错误','context':'域名或者用户名数据库中存在'})
		elif not request.POST.has_key('choice'):
			return render(request,'error.html',{'title':'发生错误','context':'weishuru neirong'})
		else:
			ppassword=request.POST['ppassword']
			duration_time=request.POST['choice']
			#计算选择的时间
			if duration_time=='3':
				productprice=0
			else:
			#修改余款（带增加）
			#主机价格
				productprice=products.hostprice*(int(duration_time)/365.0)
			#读取用户
			userm=UserProfile.objects.get(user_id=id)
			#读取用户金额
			usermoney=userm.usermoney
			#计算用户剩余金额
			newmoney=usermoney-productprice
			if newmoney>=0:
				#修改金额
				try:
					q=UserProfile.objects.update(usermoney=newmoney)
					try:
						packageaccount=products.hostpackage.zoneaccount
						packageurl=products.hostpackage.zoneurl
						packagepasswd=products.hostpackage.zonepassword
						packagepack=products.hostproperty
						#管理员设置
						whm=client.Client(packageaccount,packageurl,access_hash=packagepasswd)
						calldata=whm.call_v1('createacct',username=paccount,domain=domain,password=ppassword,plan=packagepack)
						#输出完整字符
						calldatameta=calldata['metadata']['output']
						if calldatameta['raw']==None:
							return render(request,'error.html',{'title':'发生错误','context':calldata['metadata']['reason']})
						else:
							#保存主机
							p=PersonHost(products=products,domain=domain,ppassword=ppassword,paccounts=paccount,duration_time=duration_time)
							p.user=user
							p.save()
							return render(request,'error.html',{'title':'恭喜您','context':'购买成功请进入客户中心查看'})
					except Exception as e:
						return render(request,'error.html',{'title':'发生错误','context':e})
				except:
					return render(request,'error.html',{'title':'发生错误','context':'系统扣费失败'})
				#创建账单
				b=Personblling(billingstatus=True,billingmoney=productprice)
				b.user=user
				b.save()
				return render(request,'hostktdetail.html',calldatameta)
			else:
				return render(request,'error.html',{'title':'发生错误','context':'金额不足'})
	else:
		return render(request,'error.html',{'title':'发生错误','context':'购买失败'})

#续费产品页面
def renew_product(request,personproducts_id):
	if request.user.is_authenticated():
		try:
			renewproduct=PersonHost.objects.get(id=personproducts_id)
			if renewproduct.user.id==request.user.id:
				#判断POST是否存在
				if request.POST.has_key('choice'):
					duration_time=request.POST['choice']
					productprice=renewproduct.products.hostprice*(int(duration_time)/365.0)
					id=request.user.id
					userm=UserProfile.objects.get(user_id=id)
					usermoney=userm.usermoney
					user=User.objects.get(id=id)
					newmoney=usermoney-productprice
					newtime=int(renewproduct.duration_time)+int(duration_time)
					if newmoney>=0:
						try:
							q=UserProfile.objects.update(usermoney=newmoney)
							try:
							#保存主机
								p=PersonHost.objects.filter(id=personproducts_id).update(duration_time=newtime)
							except:
								return render(request,'error.html',{'title':'发生错误','context':'续费失败'})
						except:
							return render(request,'error.html',{'title':'发生错误','context':'扣费失败'})
						#创建账单
						b=Personblling(billingstatus=True,billingmoney=productprice)
						b.user=user
						b.save()
						return render(request,'error.html',{'title':'恭喜您','context':'开通成功'})
					else:
						return render(request,'error.html',{'title':'发生错误','context':'金额不足'})
				else:
					context={'renewproduct':renewproduct}
					return render_to_response('renewone.html',context,context_instance=RequestContext(request)) 
			else:
				return render(request,'error.html',{'title':'发生错误','context':'错误情况不详，请您与管理员联系'})
		except Exception as e:
			return render(request,'error.html',{'title':'发生错误','context':e})
	else:
		return render(request,'error.html',{'title':'发生错误','context':'错误情况不详，请您与管理员联系'})


#添加商品到购物车
def add_cart(request):
	if request.user.is_authenticated():
		try:
			host=request.POST.get('hosts',None)
			try:
				products=HostProducts.objects.get(pk=host)
			except HostProducts.DoesNotExist:
				return HttpResponseRedirect(reverse('view_cart'))
			cart=request.session.get(request.user.id, None)
			if not cart:
				cart=Cart()
				cart.addproduct(products)
				request.session[request.user.id]=cart
			else:
				cart.addproduct(products)
				request.session[request.user.id]=cart
		except Exception as e:
			return HttpResponse(e)
		cart=request.session[request.user.id]
		context={'cart':cart}
		return render(request,'check.html',context)
	else:
		return HttpResponse("妈的不存在3")

#清空购物车
def clean_cart(request):
	if request.user.is_authenticated():
		cart = Cart()
		request.session[request.user.id] = cart
		cart=request.session[request.user.id]
		context={'cart':cart}
		return render(request, 'check.html', context)
	else:
		return HttpResponse("清空购物车参数")


#查看购物车
def view_cart(request):
	if request.user.is_authenticated():
		cart = request.session.get(request.user.id, None)
		cart=request.session[request.user.id]
		context={'cart':cart}
		return render(request, 'check.html', context)
	else:
		return HttpResponse("妈的不存在4")