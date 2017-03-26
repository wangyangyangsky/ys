#-*- coding: utf-8-*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#1、图片表
class Image(models.Model):
    imageId = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)
    img = models.FileField(upload_to="picture")

#2、栏目表
class Column(models.Model):
    columnId = models.AutoField(primary_key=True)
    parentColum = models.CharField(max_length=50)
    sort = models.IntegerField()
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    is_use = models.BooleanField(default=True)
    imageId = models.ForeignKey(Image, db_column="imageId")

#3、部门
class Department(models.Model):
    departmentId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

#4、新闻表
class News(models.Model):
    newsId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    create_date = models.DateField()
    upload_date = models.DateField(null=True)
    text = models.TextField()
    writer = models.CharField(max_length=50)
    is_stick = models.BooleanField(default=False)    #是否置顶
    imageId = models.ForeignKey(Image, db_column="imageId")
    columnId = models.ForeignKey(Column, db_column="columnId")
    departmentId = models.ForeignKey(Department, db_column="departmentId")

#5、管理员
class Administrators(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=20)
    departmentId = models.ForeignKey(Department, db_column="departmentId")
    level = models.IntegerField(null=True)

