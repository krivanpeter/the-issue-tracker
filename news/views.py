from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
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


def new_detail(request, slug=None):
    # A view which returns a single New object based on the ID(pk)
    new = get_object_or_404(New, slug=slug)
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
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
                                user=user,
                                content_type=content_type,
                                object_id=obj_id,
                                content=content_data,
                                parent=parent_obj,
                            )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    args = {
        'new': new,
        'comments': comments,
        'comment_form': form,
    }
    return render(request, "newdetail.html", args)


def create_new(request):
    if request.method == "POST":
        new_form = CreateNewForm(request.POST, request.FILES)
        if new_form.is_valid():
            form = new_form.save(commit=False)
            form.save()
            return redirect('/create-new/')
        else:
            print(new_form.errors)
            return redirect('/create-new/')
    else:
        new_form = CreateNewForm()
        args = {
            'new_form': new_form
        }
        return render(request, 'create_new.html', args)