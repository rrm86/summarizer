'''Building View'''
from django.shortcuts import render
from gensim.summarization.summarizer import summarize
from summarizer.models import Summarizer



def root(request):
    return render(request, "summarizer/home.html")


def result(request):
    title = request.GET["title"]
    original = request.GET["fulltext"]
    summarized_split = summarize(original, split=True, ratio=0.3)
    response = {"title": title, "split": summarized_split}
    model = Summarizer(title=title, original=original, summarized=summarized_split)
    model.save()

    return render(request, "summarizer/result.html", response)
