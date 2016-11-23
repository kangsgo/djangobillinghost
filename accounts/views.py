#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse

from alipay import Alipay

#系统自带
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
import urllib
import random
from django.views.decorators.csrf import csrf_exempt
from math import floor
#自写
from .models import  UserProfile,Deposit
from myhost.models import PersonHost,Personblling,SiteSet

# Create your views here.
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#数字字母检测
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', '只有数字与字母被允许.')

#用户信息
def index(request):
	if request.user.is_authenticated():
		u=request.user.id
		u_add=User.objects.get(id=u)
		u_info=UserProfile.objects.get(user_id=u)
		p_info=PersonHost.objects.filter(user_id=u)
		b_info=Personblling.objects.filter(user_id=u)
		context={'u_add':u_add,'u_info':u_info,'p_info':p_info,'b_info':b_info}
		return render(request,'user_index.html',context)
	else:
		return HttpResponseRedirect(reverse('signin'))

def user_info(request, user_id):
	u=User.objects.get(id=user_id)
	#提取账户余额
	u_info=UserProfile.objects.get(id=user_id)


	if not  UserProfile.objects.filter(user_id=u.id).exists():
		p=UserProfile()
		p.user=u
		p.save()

	context={'user':u,'user_info':u_info}

	return render(request,'user_info.html',context)

#用户注册
def user_reg(request):
	if request.method == 'GET':
		return render_to_response('reg.html',{},context_instance=RequestContext(request))
	elif request.method == 'POST':
		username = request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		password2=request.POST['password2']

		try:
			alphanumeric(username)
		except:
			messages.add_message(request, messages.WARNING,'用户名只能包含数字和字母')
			return HttpResponseRedirect(reverse('reg'))
		if User.objects.filter(username=username).exists():
			messages.add_message(request, messages.WARNING, '用户名已经存在')
			return HttpResponseRedirect(reverse('reg'))

		if password != password2 or password == '' or password2 == '':
			messages.add_message(request, messages.WARNING, '密码不匹配或为空')
			return HttpResponseRedirect(reverse('reg'))

		user=User.objects.create_user(username,email,password)
		user = authenticate(username=username,password=password)
		login(request, user)
		p=UserProfile()
		p.user=user
		p.save()
		return HttpResponseRedirect(reverse('index'))

#用户登陆
def user_login(request):
	if request.method == 'GET':
		return render_to_response('login.html', {},
			context_instance=RequestContext(request))
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if not User.objects.filter(username=username).exists():
			messages.add_message(request, messages.WARNING, '用户名不存在')
			return HttpResponseRedirect(reverse('signin'))

		if user is None:
			messages.add_message(request, messages.WARNING, '密码错误')
			return HttpResponseRedirect(reverse('signin'))

		login(request, user)
		return HttpResponseRedirect(reverse('index'))

#注销用户
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

#修改密码
def change_password(request):
	u = request.user
	if request.method == 'GET':
		return render_to_response('change-password.html', {},
			context_instance=RequestContext(request))
	elif request.method == 'POST':
		old = request.POST['old-password']
		new = request.POST['password']
		if request.POST['password'] != request.POST['password2'] or request.POST['password'] == '' or request.POST['password2'] == '':
			messages.add_message(request, messages.WARNING, '密码不匹配或者为空')
			return HttpResponseRedirect(reverse('password_reset'))

		if authenticate(username=u.username, password=old):
			u.set_password(new)
			u.save()
			return render(request,'error.html',{'title':'恭喜您','context':'修改密码成功' })
		else:
			messages.add_message(request, messages.WARNING, '未修改您的密码')
			return HttpResponseRedirect(reverse('password_reset'))

#充值
def money_deposit(request):
	if request.user.is_authenticated():
		return render_to_response('addmoney.html',{},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect(reverse('signin'))

#充值反馈页面
def money_check(request):
	if request.user.is_authenticated():
		id=request.user.id
		personmoney=UserProfile.objects.get(user_id=id)
		try:
			money=request.POST['counp']
		except Exception as e:
			return HttpResponse(e)
		if Deposit.objects.filter(counpon=money,counponactive=True):
			c=Deposit.objects.filter(counpon=money,counponactive=True).update(counponactive=False)
			d=Deposit.objects.get(counpon=money)
			personnewmoney=personmoney.usermoney+d.counmoney
			m=UserProfile.objects.filter(user_id=id).update(usermoney=personnewmoney)
			return render(request,'error.html',{'title':'恭喜您','context':'充值成功' })
		else:
			return render(request,'error.html',{'title':'发生错误','context':'代金卷未发现或已失效' })
	else:
		return HttpResponseRedirect(reverse('signin'))

alipay=Alipay(pid='zzz',key='zzz',seller_email='zzz@qq.com')
#set alipay
def trade_check(request):
	'''doc https://github.com/lxneng/alipay'''
	if request.user.is_authenticated():
		if request.method == 'GET':
			return render_to_response('change-password.html', {},
				context_instance=RequestContext(request))
		elif request.method == 'POST':	
			try:
				money=request.POST['money']
				try:
					if int(money)>=0:
						id=request.user.id
						subject='balance'
						d=str(id)+'6000'+str(random.randint(0,6000))
						return_url='http://www.billvm.com/accounts/return_url/'
						notify_url='http://www.billvm.com/accounts/notify_url/'
						a=Personblling.objects.create(user_id=id,billingmoney=money,billingstatus=False,trade_no=d)
						#b=UserProfile.objects.get(user_id=id)
						#c=int(b.usermoney)+int(money)
						#d=UserProfile.objects.filter(user_id=id).update(usermoney=c)
						apliyurl=alipay.create_direct_pay_by_user_url(out_trade_no=d,subject=subject,total_fee=money,return_url=return_url,notify_url=notify_url)
						return HttpResponseRedirect(apliyurl)
					else:
						return render(request,'error.html',{'title':'发生错误','context':'金额不正确或未输入' })
				except Exception as e:
					return render(request,'error.html',{'title':'发生错误','context':e })
			except:
				return render(request,'error.html',{'title':'发生错误','context':'金额不正确或未输入' })
	else:
		return HttpResponseRedirect(reverse('signin'))

@csrf_exempt
def notify_url_handler(request):
	'''doc http://blog.csdn.net/hornbills/article/details/40338949'''
	if request.method=='POST':
		if alipay.verify_notify(**request.POST.dict()):
			trade_no=request.POST.get('out_trade_no')  
			total_fee=request.POST.get('total_fee')
			total_fee2=floor(float(total_fee))
			a=Personblling.objects.filter(trade_no=trade_no).update(billingstatus=True)
			g=Personblling.objects.get(trade_no=trade_no)
			e=g.user.id
			b=UserProfile.objects.get(user=e)
			c=int(b.usermoney)+total_fee2
			d=UserProfile.objects.filter(user=e).update(usermoney=c)
			return HttpResponse("success")
		else:
			return HttpResponse("failed")
	else:
		return HttpResponse("failed")

def return_url_handler(request):
	if alipay.verify_notify(**request.GET.dict()):
		tn=request.GET.get('out_trade_no')
		trade_no = request.GET.get('trade_no')
		trade_status = request.GET.get('trade_status') 
		return render(request,'error.html',{'title':'恭喜您','context':'支付成功' })
	else:
		return render(request,'error.html',{'title':'抱歉','context':'发生错误' })