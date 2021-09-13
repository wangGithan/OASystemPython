from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def login_form(request):
    request.encoding = 'utf-8'
    if 'inputEmail' in request.POST and request.POST['inputEmail']:
        message = '你搜索的内容为: ' + request.POST['inputEmail']
    else:
        message = '你提交了空表单'
    print(message)
    return HttpResponse(message)
    #return render(request, 'user.html')
