# -*-coding: utf-8-*-
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from admina import models

@csrf_exempt
def img(req):
    '''
    返回添加图片界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/img.html")

@csrf_exempt
def img_form(req):
    '''
    返回图片管理界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/img_form.html")

@csrf_exempt
def index(req):
    return render_to_response("admina/index.html")

@csrf_exempt
def add_news(req):
    '''
    返回添加新闻界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/add_news.html")

@csrf_exempt
def check_news(req):
    '''
    返回查看新闻界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/check_news.html")

@csrf_exempt
def add_admin(req):
    '''
    返回添加管理员界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/add_admin.html")

@csrf_exempt
def check_admin(req):
    '''
    返回查看管理员界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/check_admin.html")

@csrf_exempt
def col_page1(req):
    '''
    返回添加栏目界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/col_page1.html")

@csrf_exempt
def col_page2(req):
    '''
    返回查看栏目界面
    :param req: 
    :return: 
    '''
    return render_to_response("admina/col_page2.html")

@csrf_exempt
def login(req):
    '''
    登录函数
    :param req: 
    :return: 
    '''
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        administrators = models.Administrators.objects.filter(username=username)
        if administrators.count() == 0:
            return HttpResponse(0)
        elif administrators.password == password:
            return render_to_response("admina/index.html")
        else:
            return HttpResponse(1)
    else:
        return render_to_response("admina/login.html")

@csrf_exempt
def create_admin(req):
    '''
    创建管理员
    :param req: 
    :return: 
    '''
    pass




