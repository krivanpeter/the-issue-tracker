from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from accounts.models import UserProfile
from comments.forms import CommentForm
from comments.models import Comment
from .models import New
from .forms import CreateNewForm


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


def new_detail(request, pk):
    # A view which returns a single New object based on the ID(pk)
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


def create_new(request):
    if request.method == "POST":
        new_form = CreateNewForm(request.POST)
        if new_form.is_valid():
            new_form = new_form.save(commit=False)
            new_form.save()
            return redirect('/news/')
        else:
            return redirect('/news/')
    else:
        new_form = CreateNewForm()
        args = {
            'new_form': new_form
        }
        return render(request, 'create_new.html', args)