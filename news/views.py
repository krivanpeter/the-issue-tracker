from django.shortcuts import render, get_object_or_404
from .models import New
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


'''
A view which shows all the news
'''
@login_required
def all_news(request):
    news_list = New.objects.all().order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 5)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'news': news})


'''
A view which returs a single New object based on the ID(pk)
'''
def new_detail(request, pk):
    new = get_object_or_404(New, pk=pk)
    new.views += 1
    new.save()
    return render(request, "newdetail.html", {'new':new})