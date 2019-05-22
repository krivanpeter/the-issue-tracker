from django.shortcuts import render
from .models import New
from django.contrib.auth.decorators import login_required


@login_required
def all_news(request):
    news = New.objects.all()
    return render(request, "news.html", {"news": news})