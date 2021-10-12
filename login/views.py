from django.http import HttpResponse
from employee.models import Users
import json
import secrets


# Create your views here.
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def login_form(request):
    #response = {}
    response_data = {}
    try:
        request.encoding = 'utf-8'
        postBody = request.body
        user = json.loads(postBody)
        user_queryset = Users.objects.all().filter(userloginname=user['userloginname'], userpass=user['userpass'])
        if user_queryset.exists():
            token = secrets.token_hex()
            print(token)
            response_data['token'] = token
            response_data['error_num'] = 0
            response_data['msg'] = 'success'
        else:
            response_data['error_num'] = 2
            response_data['msg'] = 'wrong loginName or password'
    except Exception as e:
        response_data['msg'] = str(e)
        response_data['error_num'] = 1
    #return JsonResponse(response)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
