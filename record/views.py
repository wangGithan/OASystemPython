from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from record.models import WorkTime
import json
from django.db.models import Q
from django.core import serializers
import datetime


# Create your views here.

def record(request):
    response_data = {}
    userid = request.GET.get('userid')
    user_queryset = WorkTime.objects.all().filter(Q(userid=userid, work_end__isnull=True) | Q(userid=userid, work_end=""))
    if user_queryset.exists():
        response_data['error_num'] = 0
        response_data['status'] = "begin"
    else:
        response_data['error_num'] = 0
        response_data['status'] = "end"
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def make_record(request):
    response_data = {}
    try:
        record = json.loads(request.body)
        if record['startTime'] != "":
            #date_string = record['startTime'].split(" ")
            #work_data = date_string[0].replace("/", "-")
            # 添加record到数据库
            WorkTime.objects.create(userid=record['userid'], work_begin=record['startTime'])

        else:
            userid = record['userid']
            #date_string = record['endTime'].split(" ")
            #work_data = date_string[0].replace("/", "-")
            # 添加endtime到数据库
            user_queryset = WorkTime.objects.all().filter(Q(userid=userid, work_end__isnull=True) | Q(userid=userid, work_end="")).first()
            print(user_queryset.work_begin)
            startTime = datetime.datetime.strptime(user_queryset.work_begin, "%Y/%m/%d %H:%M")
            endTime = datetime.datetime.strptime(record['endTime'], "%Y/%m/%d %H:%M")
            user_queryset.work_end = record['endTime']
            #计算时间差
            user_queryset.total = endTime - startTime
            user_queryset.save()
        response_data['msg'] = 'success'
        response_data['error_num'] = 0
    except Exception as e:
        response_data['msg'] = str(e)
        response_data['error_num'] = 1
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def check_record(request):
    response_data = {}
    userid = request.GET.get('userid')
    user_queryset = WorkTime.objects.all().filter(userid=userid)
    print(user_queryset)
    response_data['list'] = json.loads(serializers.serialize("json", user_queryset))
    response_data['msg'] = 'success'
    response_data['error_num'] = 0
    return HttpResponse(json.dumps(response_data), content_type="application/json")

