from django.shortcuts import render
from summarizer.models import Summarizer

def Root(request):
    return render(request,'summarizer/home.html')
    