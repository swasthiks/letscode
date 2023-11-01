
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('contact', views.contact,name="contact"),
    path('about', views.about,name="about"),
    path('home',views.home,name="home"),
    path('search',views.search,name="search"),
    path('',views.home,name="home"),
    path('signup',views.handleSigup,name="handlesignup"),
    path('login',views.handleLogin,name="handleLogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    
]
