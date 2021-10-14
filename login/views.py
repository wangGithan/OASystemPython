from django.http import HttpResponse
from employee.models import Users
import json
import secrets


# Create your views here.
from django.shortcuts import render

#OASystem/login/templates/login.html用
def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    elif (request.method == 'POST'):
        response_data = {}
        try:
            request.encoding = 'utf-8'
            user_queryset = Users.objects.all().filter(userloginname=request.POST['userName'], userpass=request.POST['password'])
            if user_queryset.exists():
                token = secrets.token_hex()
                response_data['token'] = token
                response_data['error_num'] = 0
                response_data['msg'] = 'success'
                response_data['userId'] = user_queryset[0].userid
                response_data['userName'] = user_queryset[0].username
            else:
                response_data['error_num'] = 2
                response_data['msg'] = 'wrong loginName or password'
        except Exception as e:
            response_data['msg'] = str(e)
            response_data['error_num'] = 1
    return HttpResponse(json.dumps(response_data), content_type="application/json")




#OASystem/frontend/src/components/Login.vue用
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
            response_data['userId'] = user_queryset[0].userid
            response_data['userName'] = user_queryset[0].username
        else:
            response_data['error_num'] = 2
            response_data['msg'] = 'wrong loginName or password'
    except Exception as e:
        response_data['msg'] = str(e)
        response_data['error_num'] = 1
    #return JsonResponse(response)
    return HttpResponse(json.dumps(response_data), content_type="application/json")
