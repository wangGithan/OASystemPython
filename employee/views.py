from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from employee.models import Users


def employee(request):
    user_queryset = Users.objects.all()
    return render(request, 'user.html', {"user_queryset": user_queryset})


def user_list(request):
    #user_queryset = Users.objects.all()
    #return render(request, 'user.html', {"user_queryset": user_queryset})
    print('oo')



