# -*-coding :utf-8-*-
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(req):
    return render_to_response("admina/login.html")

@csrf_exempt
def index(req):
    return render_to_response("admina/index.html")

@csrf_exempt
def col_page1(req):
    return render_to_response("admina/col_page2.html")



@csrf_exempt
def add_news(req):
    pass