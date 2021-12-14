from django.contrib import  admin
from django.urls import path 
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path('home', views.home, name = 'home'),
    path('logout', views.logout, name = 'logout'),
    path('register', views.registration, name = 'register')

]