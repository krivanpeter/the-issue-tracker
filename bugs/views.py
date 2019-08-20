from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from accounts.models import UserProfile
from comments.forms import CommentForm
from comments.models import Comment
from .models import Bug, BugImages
from .forms import BugReportForm, BugImageForm



@login_required
def all_bugs(request):
    # A view which shows all the reported bugs,
    # ordered by the number of upvotes and the date of the report
    if request.user.is_authenticated:
        bug_list = Bug.objects.annotate(count=Count('upvotes')).order_by('-count')
        page = request.GET.get('page', 1)
        paginator = Paginator(bug_list, 10)
        try:
            bugs = paginator.page(page)
        except PageNotAnInteger:
            bugs = paginator.page(1)
        except EmptyPage:
            bugs = paginator.page(paginator.num_pages)
        return render(request, "bugs.html", {"bugs": bugs})
    else:
        return redirect('index')


def bug_detail(request, slug=None):
    # A view which returns a single Bug object based on the ID(pk)
    if request.user.is_authenticated:
        bug = get_object_or_404(Bug, slug=slug)
        comments = bug.comments
        initial_data = {
            "content_type": bug.get_content_type,
            "object_id": bug.id
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
            'bug': bug,
            'comments': comments,
            'comment_form': form,
        }
        return render(request, "bugdetail.html", args)
    else:
        return redirect('index')


def report_bug(request):
    # A view which allows the user to report new bugs
    if request.user.is_authenticated:
        if request.method == "POST":
            new_bug_form = BugReportForm(request.POST)
            bug_img_form = BugImageForm(request.POST, request.FILES)

            if new_bug_form.is_valid() and bug_img_form.is_valid():
                bug_form = new_bug_form.save(commit=False)
                bug_form.reported_by = UserProfile.objects.get(user=request.user)
                bug_form.save()

                for index, file in enumerate(request.FILES.getlist('images')):
                    if index == 3:
                        break
                    instance = BugImages(
                        bug=bug_form,
                        image=file
                    )
                    instance.save()
                return redirect('/bugs/')
            else:
                data = {'is_valid': False}
                return JsonResponse(data)
        else:
            new_bug_form = BugReportForm()
            bug_img_form = BugImageForm()
            args = {
                'new_bug_form': new_bug_form,
                'bug_img_form': bug_img_form
            }
            return render(request, 'reportbug.html', args)
    else:
        return redirect('index')


def upvote_bug(request, slug=None):
    # A view which allows the user to like and unlike bugs
    if request.user.is_authenticated:
        data = {'user_upvoted': False}
        bug = get_object_or_404(Bug, slug=slug)
        user = request.user
        if user.is_authenticated():
            if user in bug.upvotes.all():
                bug.upvotes.remove(user)
                data['user_upvoted'] = False
            else:
                bug.upvotes.add(user)
                data['user_upvoted'] = True
        return JsonResponse(data)
    else:
        return redirect('index')