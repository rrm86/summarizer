from django.urls import path
from summarizer import views

urlpatterns = [
    path('result/',views.Result, name='result'),
    path('',views.Root)
]
