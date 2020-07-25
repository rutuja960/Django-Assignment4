
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('addpage', views.addpage,name="addpage"),
    #path('check',views.getdata,name="getdata"),
    

]
