#coding=utf-8
from django.shortcuts import render,HttpResponse

# Create your views here.
#定义首页
def index(request):
	return  render (request,'home_index.html',{})

def about_us(request):
	return  render (request,'about_me.html',{})

def tos(request):
	return  render (request,'tos.html',{})