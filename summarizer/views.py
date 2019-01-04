from django.shortcuts import render
from summarizer.models import Summarizer
from gensim.summarization.summarizer import summarize


def Root(request):
    return render(request, "summarizer/home.html")


def Result(request):
    title = request.GET["title"]
    original = request.GET["fulltext"]
    summarized = summarize(original)
    summarized_split = summarize(original, split=True, ratio=0.3)
    response = {"title": title, "fulltext": summarized, "split":summarized_split}
    model = Summarizer(title=title, original=original, summarized=summarized)
    model.save()

    return render(request, "summarizer/result.html", response)

