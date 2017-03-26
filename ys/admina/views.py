# -*-coding: utf-8-*-
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from admina import models

@csrf_exempt
def index(req):
    return render_to_response("admina/index.html")

@csrf_exempt
def add_news(req):
    return render_to_response("admina/add_news.html")

@csrf_exempt
def check_news(req):
    return render_to_response("admina/check_news.html")

@csrf_exempt
def add_admin(req):
    return render_to_response("admina/add_admin.html")

@csrf_exempt
def check_admin(req):
    return render_to_response("admina/check_admin.html")

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
    pass

@csrf_exempt
def col_page1(req):
    return render_to_response("admina/col_page2.html")


