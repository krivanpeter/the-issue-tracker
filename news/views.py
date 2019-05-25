from django.shortcuts import render
from .models import New
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


'''
A view which shows all the news
'''
@login_required
def all_news(request):
    news_list = New.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 5)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'news': news})


