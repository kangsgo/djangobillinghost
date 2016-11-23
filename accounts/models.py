#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
import urllib
import hashlib
# Create your models here.

#账户信息
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	nickname=models.CharField(max_length=12, blank=True, null=True,verbose_name='用户昵称')
	use_gravatar=models.BooleanField(default=True)
	avatar_url=models.URLField(blank=True, null=True)
	usermoney=models.IntegerField(default=0,verbose_name='用户余额')
	def unread_mention(self):
		return self.user.received_mentions.filter(read=False)

	def old_mention(self):
		return self.user.received_mentions.filter(read=True)[0:5]

	def __unicode__(self):
		return self.user.username

	class Meta:
		verbose_name = '用户名'
		verbose_name_plural=verbose_name
		ordering = ['id']

	#用户头像
	def avatar(self):
		da=''
		dic={}
		if self.use_gravatar:
			mail=self.user.email.lower()
			gravatar_url="http://www.gravatar.com/avatar/"
			base_url = gravatar_url + hashlib.md5(mail).hexdigest() + "?"
			dic['small'] = base_url + urllib.urlencode({'d': da, 's': '40'})
			dic['middle'] = base_url + urllib.urlencode({'d': da, 's': '48'})
			dic['large'] = base_url + urllib.urlencode({'d': da, 's': '80'})
			return dic
		elif self.avatar_url:
			dic['small']=self.avatar_url
			dic['middle']=self.avatar_url
			dic['large']=self.avatar_url
		return dic

#代金卷
class Deposit(models.Model):
	counpon=models.CharField(max_length=15,blank=True, null=True,verbose_name='代金卷')
	#默认为有效,使用后变为无效
	counponactive=models.BooleanField(default=True)
	counmoney=models.IntegerField(default=0,verbose_name='金额')

	def __unicode__(self):
		return self.counpon

	class Meta:
		verbose_name = '代金卷'
		verbose_name_plural=verbose_name
		ordering = ['id']

		