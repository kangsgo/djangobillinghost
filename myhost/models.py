#coding=utf-8
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from hosts.models import  HostProducts,HostZone

# Create your models here.

class PersonHost(models.Model):
	'''每个人的主机'''
	user = models.ForeignKey(User,related_name='myproduct')
	products=models.ForeignKey(HostProducts, verbose_name='产品套餐')
	domain=models.CharField(max_length=30,blank=True, null=True,verbose_name='产品域名')
	create_date=models.DateTimeField(auto_now_add=True)
	duration_time=models.IntegerField(default=0)
	STATUS_CHOICES=(
		('Y','active'),
		('P','Pengding'),
		('N','Delete'),
		)
	products_status=models.CharField(max_length=2,choices=STATUS_CHOICES,default='P')
	paccounts=models.CharField(max_length=20,blank=True, null=True,verbose_name='产品账户名')
	ppassword=models.CharField(max_length=20,blank=True, null=True,verbose_name='产品密码')


	#到期时间
	def come_time(self):
		a=int(self.duration_time)
		return self.create_date+datetime.timedelta(days=a)
	#判断是否到期
	def was_come_time(self):
		a=int(self.duration_time)
		return self.create_date+datetime.timedelta(days=a) <= timezone.now()
		was_come_time.short_description = '是否到期'
		was_published_recently.boolean = True

	class Meta:
		verbose_name='个人主机'
		verbose_name_plural = verbose_name
		ordering =['create_date'] 

	def __unicode__(self):
		return str(self.id)

class Personblling(models.Model):
	'''个人账单'''
	user = models.ForeignKey(User,related_name='myblling')
	billingdate=models.DateTimeField(auto_now_add=True)
	billingmoney=models.IntegerField(default=0,verbose_name='账单金额')
	billingstatus=models.BooleanField(default=False,verbose_name='是否付款')
	trade_no=models.CharField(max_length=50,default=0,verbose_name='jiaoyihao')

	class Meta:
		verbose_name='个人账单'
		verbose_name_plural = verbose_name
		ordering =['billingdate'] 

	def __unicode__(self):
		return str(self.id)

class SiteSet(models.Model):
	'''yuming'''
	sitedomain=models.CharField(max_length=50,default='http://billvm.com',verbose_name='zhandianyuming')
