from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee),
    path('add_user/', views.add_user),
    path('search_user/', views.search_user),
    path('edit_user/', views.edit_user),
    path('del_user/', views.del_user),


]
