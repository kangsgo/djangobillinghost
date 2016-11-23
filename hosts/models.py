#coding=utf-8
from django.db import models

# Create your models here.

class HostZone(models.Model):
	"""产品地区"""
	zonename=models.CharField(max_length=30,verbose_name='产品地区')
	zoneurl=models.CharField(max_length=100,blank=True, null=True,verbose_name='服务器地址')
	zoneaccount=models.CharField(max_length=50,blank=True, null=True,verbose_name='服务器名')
	ssh=models.CharField(max_length=5,default='2083',verbose_name='服务端口')
	zonepassword=models.TextField(blank=True, null=True,verbose_name='服务器密钥')
	#服务器类型接口，等待完善
	HOST_CHOICES=(
		('cpanel','cpanel'),
		)
	servertype=models.CharField(max_length=2,choices=HOST_CHOICES,default='cpanel',verbose_name='服务器类型')

	class Meta:
		verbose_name = '地区'
		verbose_name_plural=verbose_name
		ordering = ['id']

	def __unicode__(self):
		return self.zonename


class HostProducts(models.Model):
	"""产品分类"""
	hostname=models.CharField(max_length=30, verbose_name='产品名称')
	hostpackage=models.ForeignKey(HostZone, verbose_name='产品地区')
	hostsize=models.IntegerField(default=0,verbose_name='空间大小')
	hosttraffic=models.IntegerField(default=0,verbose_name='月流量')
	hostprice=models.FloatField(default=0,verbose_name='产品价格')
	hostproperty=models.CharField(max_length=30,blank=True, null=True,verbose_name='套餐属性')
	hostdesc=models.CharField(max_length=100,verbose_name='产品简介')

	class Meta:
		verbose_name = '产品'
		verbose_name_plural=verbose_name
		ordering = ['id']

	def __unicode__(self):
		return self.hostname

#购物车条目
class Caritem(models.Model):
	products=models.ForeignKey(HostProducts, verbose_name='购物车条目')
	quantity=models.IntegerField(default=0, verbose_name='数量')
	sum_price=models.FloatField(default=0, verbose_name='小计')

	class Meta:
		verbose_name='购物车条目'
		verbose_name_plural=verbose_name

	def __unicode__(self):
		return str(self.id)


#购物车
class Cart(object):
	def __init__(self):
		self.items=[]
		self.totnameal_price=0.0

	def addproduct(self, products):
		self.total_price += products.hostprice
		for item in self.items:
			if item.products.id == products.id:
				item.quantity +=1
				item.sum_price += products.hostprice
				return
		else:
			self.items.append(Caritem(products=products,quantity=1,sum_price=products.hostprice))