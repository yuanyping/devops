from django.contrib import admin
from django.urls import path,include,re_path
from user import views

urlpatterns = [
    # re_path("^",views.login),
    path('login/',views.login),
    path('loginout/',views.loginout),

]