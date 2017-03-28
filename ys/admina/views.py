#-*-coding: utf-8-*-
import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from admina import models

@csrf_exempt
def index(req):
    return render_to_response("admina/index.html")

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
        elif administrators[0].password == password:
            return HttpResponse(2)
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
    if req.method == "POST":
        username = req.POST["username"]
        administrators = models.Administrators.objects.filter(username=username)
        if administrators.count() == 0:
            name = req.POST["name"]
            password = req.POST["password"]
            department = req.POST["department"]
            departments = models.Department.objects.filter(name=department)
            if departments.count() == 0:
                depart = models.Department(name=department).save()
                admin = models.Administrators(
                    username=username, name=name, password=password, departmentId=depart.departmentId
                ).save()
            else:
                admin = models.Administrators(
                    username=username, name=name, password=password, departmentId_id=departments[0].departmentId
                ).save()
            return HttpResponse(1)
        else:
            return HttpResponse(0)
    else:
        return render_to_response("系统错误！！！！")

@csrf_exempt
def inspect_admin(req):
    '''
    查看管理员
    :param req: 
    :return: 
    '''
    Administrators = models.Administrators.objects.all()
    list = []
    for obj in Administrators:
        department = models.Department.objects.filter(departmentId=obj.departmentId_id)
        infor = {
            "name": obj.name, "department": department[0].name,
            "username": obj.username, "password": obj.password, "is_use": obj.is_use
        }
        list.append(infor)
    return HttpResponse(json.dumps(list))

@csrf_exempt
def create_column(req):
    '''
    添加栏目
    :param req:
    :return:
    '''
    pass
