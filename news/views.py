from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from comments.forms import CommentForm
from comments.views import create_comment
from .models import New
from .forms import CreateNewForm


'''
A view which shows all the news
'''
@login_required
def all_news(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('index')


def new_detail(request, slug=None):
    if request.user.is_authenticated:
        # A view which returns a single New object based on the ID(pk)
        new = get_object_or_404(New, slug=slug)
        new.views += 1
        new.save()
        comments = new.comments
        initial_data = {
            "content_type": new.get_content_type,
            "object_id": new.id
        }
        form = CommentForm(request.POST or None, initial=initial_data)
        create_comment(request, form)
        args = {
            'new': new,
            'comments': comments,
            'comment_form': form,
        }
        return render(request, "newdetail.html", args)
    else:
        return redirect('index')


def create_new(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('index')