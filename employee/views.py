# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render
from employee.models import Users
from django.core import serializers
import json
import datetime
import re


def employee(request):
    response = {}
    try:
        user_queryset = Users.objects.all()
        response['list'] = json.loads(serializers.serialize("json", user_queryset))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    # return render(request, 'user.html', {"user_queryset": user_queryset})
    return JsonResponse(response)


def add_user(request):
    response = {}
    try:
        if(request.method == 'POST'):
            postBody = request.body
            user = json.loads(postBody)
            print(type(user))  #dic
            user['userbirth'] = getBirth(user['userbirth'])
            user['userage'] = getAge(user['userbirth'])
            #添加user到数据库
            create = Users.objects.create(**user)  #加了两个星号 ** 的参数会以字典的形式导入。
            print(create.pk)
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    #return render(request, 'user.html')


def search_user(request):
    response = {}
    try:
        user_name = request.GET.get('user_name')
        if user_name == '':
            user_queryset = Users.objects.all()
        else:
            user_queryset = Users.objects.all().filter(username=user_name)
        response['list'] = json.loads(serializers.serialize("json", user_queryset))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    #return render(request, 'user.html')


def edit_user(request):
    response = {}
    if (request.method == 'GET'):
        try:
            userid = request.GET.get('userid')
            user_queryset = Users.objects.all().filter(userid=userid)
            response['list'] = json.loads(serializers.serialize("json", user_queryset))
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1

    elif(request.method == 'POST'):
        try:
            postBody = request.body
            user = json.loads(postBody)
            print(type(user))  # dic
            user['userbirth'] = getBirth(user['userbirth'])
            user['userage'] = getAge(user['userbirth'])
            # 添加user到数据库
            #create = Users.objects.create(**user)  # 加了两个星号 ** 的参数会以字典的形式导入。
            update = Users.objects.filter(userid=user['userid']).update(**user)
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1


    return JsonResponse(response)


def del_user(request):
    response = {}
    try:
        userid = request.GET.get('userid')
        obj = Users.objects.get(userid=userid)
        obj.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def getBirth(birthYear):
    #Thu Jun 23 1983 00:00:00 GMT+0900 (日本标准时间)
    if re.match("\d\d\d\d\-\d\d\-\d\d", birthYear):
        birthYear = datetime.datetime.strptime(birthYear, "%Y-%m-%d")
        return birthYear
    data = birthYear.split(' ')
    if data[1] == 'Jan':
        month = '01'
    elif data[1] == 'Feb':
        month = '02'
    elif data[1] == 'Mar':
        month = '03'
    elif data[1] == 'Apr':
        month = '04'
    elif data[1] == 'May':
        month = '05'
    elif data[1] == 'Jun':
        month = '06'
    elif data[1] == 'Jul':
        month = '07'
    elif data[1] == 'Aug':
        month = '08'
    elif data[1] == 'Sep':
        month = '09'
    elif data[1] == 'Oct':
        month = '10'
    elif data[1] == 'Nov':
        month = '11'
    elif data[1] == 'Dec':
        month = '12'
    birthYear = data[3]+"-"+month+"-"+data[2]
    birthYear = datetime.datetime.strptime(birthYear, "%Y-%m-%d")
    return birthYear

def getAge(birthDay):
    # 获取年龄
    today = datetime.datetime.today()
    birth_day = birthDay.replace(year=today.year)
    if (today > birth_day):
        age = today.year - birthDay.year
    else:
        age = today.year - birthDay.year - 1
    return age
