from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from accounts.models import UserProfile
from comments.forms import CommentForm
from comments.models import Comment
from .models import New


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
    comments = new.comments
    new.views += 1
    new.save()
    initial_data = {
        "content_type": new.get_content_type,
        "object_id": new.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        user = UserProfile.objects.get(user=request.user)
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        new_comment, created = Comment.objects.get_or_create(
                                user=user,
                                content_type=content_type,
                                object_id=obj_id,
                                content=content_data
                            )
    args = {
        'new': new,
        'comments': comments,
        'comment_form': form,
    }
    return render(request, "newdetail.html", args)