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
    Identification = req.POST["Identification"]
    if Identification == "1":
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
    if Identification == "2":
        username = req.POST["username"]
        Administrators = models.Administrators.objects.filter(username=username)[0]
        department = models.Department.objects.filter(departmentId=Administrators.departmentId_id)
        list = []
        infor = {
            "name": Administrators.name, "department": department[0].name,
            "username": Administrators.username, "password": Administrators.password, "is_use": Administrators.is_use
        }
        list.append(infor)
        return HttpResponse(list)

@csrf_exempt
def create_column(req):
    '''
    添加栏目
    :param req:
    :return:
    '''
    pass

@csrf_exempt
def savepciture(img):
    '''
    上传图片  用于封装
    :param req: 
    :return: 
    '''
    url = "picture/" + str(img)
    image = models.Image(img=img, url=url)
    image.save()
    return image

@csrf_exempt
def create_column(req):
    '''
    创建栏目
    :param req: 
    :return: 
    '''
    if req.method == "POST":
        name = req.POST["name"]
        Columns = models.Column.objects.filter(name=name)
        if Columns.count() == 0:
            level = req.POST["level"]
            parentColum = req.POST["parentColum"]
            sort = req.POST["sort"]
            is_use = req.POST["is_use"]
            if is_use == 1:
                is_use = True
            elif is_use == 0:
                is_use = False
            img = req.FILES["image"]
            image = savepciture(img)
            Column = models.Column(
                parentColum=parentColum, sort=sort, level=level, name=name,
                is_use=is_use, imageId_id=image.imageId
            ).save();
            return HttpResponse(1)
        else:
            return HttpResponse(0)

@csrf_exempt
def inspect_column(req):
    '''
    查询栏目信息
    :param req: 
    :return: 
    '''
    columns = models.Column.objects.all()
    list = []
    for obj in columns:
        infor = {
            "columnId": obj.columnId, "parentColum": obj.parentColum, "sort": obj.sort,
            "level": obj.sort, "name": obj.name, "is_use": obj.is_use
        }
        list.append(infor)
    return HttpResponse(json.dumps(list))

@csrf_exempt
def delete(req):
    '''
    删除按钮
    :param req: 
    :return: 
    '''
    Identification = req.POST["Identification"]
    if Identification == "3":
        imageId = req.POST["imageId"]
        img = models.Image.objects.filter(imageId=imageId)[0].delete()
        return HttpResponse(1)
    elif Identification == "2":
        username = req.POST["username"]
        models.Administrators.objects.filter(username=username)[0].delete()
        return HttpResponse(1)
    elif Identification == "1":
        columnId = req.POST["columnId"]
        column = models.Column.objects.filter(columnId=columnId)[0]
        img = models.Image.objects.filter(imageId=column.imageId_id)[0].delete()
        return HttpResponse(1)

@csrf_exempt
def colum_info(req):
    '''
    返回栏目信息，用于侧边栏，和加载图片
    :param req: 
    :return: 
    '''
    Columns = models.Column.objects.all()
    list = []
    for obj in Columns:
        info = {"name": obj.name, "columnId": obj.columnId}
        list.append(info)
    return HttpResponse(json.dumps(list))

@csrf_exempt
def add_news_column(req):
    '''
    动态绑定添加新闻界面
    :param req: 
    :return: 
    '''
    columnId = req.GET["columnId"]
    column = models.Column.objects.filter(columnId=columnId)[0]
    return render(req, "admina/add_news.html", {"name": column.name, "columnId": column.columnId})

@csrf_exempt
def inspect_img(req):
    imgs = models.Image.objects.all()
    list = []
    for obj in imgs:
        info = {
            "url": obj.url, "img": str(obj.img), "imageId": obj.imageId
        }
        list.append(info)
    return HttpResponse(json.dumps(list))

@csrf_exempt
def save_picture(req):
    img = req.FILES["image"]
    image = savepciture(img)
    return HttpResponse(1)
