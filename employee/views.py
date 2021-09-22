# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render
from employee.models import Users
from django.core import serializers
import json
import datetime


def employee(request):
    print("employee")
    response = {}
    try:
        user_queryset = Users.objects.all()
        response['list'] = json.loads(serializers.serialize("json", user_queryset))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        print(response)
    # return render(request, 'user.html', {"user_queryset": user_queryset})
    return JsonResponse(response)


def user_list(request):
    # user_queryset = Users.objects.all()
    # return render(request, 'user.html', {"user_queryset": user_queryset})
    print('oo')


def add_user(request):
    response = {}
    try:
        if(request.method == 'POST'):
            postBody = request.body
            user = json.loads(postBody)
            print(type(user))  #dic
            #处理生日日期
            nPos = user['userbirth'].index('T')
            user['userbirth'] = datetime.datetime.strptime(user['userbirth'][0: nPos], "%Y-%m-%d")
            #获取年龄
            today = datetime.datetime.today()
            birth_day = user['userbirth'].replace(year=today.year)
            if(today > birth_day):
                user['userage'] = today.year - user['userbirth'].year
            else:
                user['userage'] = today.year - user['userbirth'].year-1
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