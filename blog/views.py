#coding=utf-8
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
	blog_list=Article.objects.all()
	context={'blog_list':blog_list}
	return render(request,'blog_index.html',context)

def blog_detail(request, id):
	try:
		post=Article.objects.get(id=str(id))
		return render(request,'blog_detail.html',{'post' : post})
	except Article.DoesNotExist:
		return render(request,'error.html',{'title':'发生错误','context':'未查找到你要找的文章'})