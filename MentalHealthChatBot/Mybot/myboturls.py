from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_register_view, name='login_register_view'),
]