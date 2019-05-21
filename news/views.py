from django.shortcuts import render
from .models import New


def all_news(request):
    news = New.objects.all()
    return render(request, "news.html", {"news": news})