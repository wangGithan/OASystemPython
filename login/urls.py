from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    #path('login_form/', views.login_form),
    path('login/', views.login),
    path('login_form/', views.login_form),
]
