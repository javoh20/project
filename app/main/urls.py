from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.Main, name = "main"),
    path('about/', views.About, name = "about"),
    path('about/contact/', views.Contact, name = "contact")
]
