from django.urls import path
from . import views


urlpatterns = [
    path('', views.record),
    path('make_record/', views.make_record),
    path('check_record/', views.check_record),

]
