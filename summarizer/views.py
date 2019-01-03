from django.shortcuts import render
from summarizer.models import Summarizer
from gensim.summarization.summarizer import summarize

def Root(request):
    return render(request,'summarizer/home.html')

def Result(request):
    email = request.GET['email']
    text = request.GET['fulltext']
    text = summarize(text)
    response = {'email':email,'fulltext':text}
    return render(request,'summarizer/result.html',response)
    