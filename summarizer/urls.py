'''Routing Urls'''
from django.urls import path
from summarizer import views

urlpatterns = [
    path('result/', views.result, name='result'),
    path('', views.root)
]
