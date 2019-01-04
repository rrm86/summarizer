from django.shortcuts import render
from summarizer.models import Summarizer
from gensim.summarization.summarizer import summarize


def Root(request):
    return render(request, "summarizer/home.html")


def Result(request):
    email = request.GET["email"]
    original = request.GET["fulltext"]
    summarized = summarize(original)
    response = {"email": email, "fulltext": summarized}
    model = Summarizer(email=email, original=original, summarized=summarized)
    model.save()

    return render(request, "summarizer/result.html", response)

