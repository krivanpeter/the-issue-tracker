from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from accounts.models import UserProfile
from comments.forms import CommentForm
from comments.models import Comment
from .models import Bug
from .forms import BugReportForm


'''
A view which shows all the reported bugs
'''
@login_required
def all_bugs(request):
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})


'''
A view which returs a single Bug object based on the ID(pk)
'''
def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
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
        new_comment, created = Comment.objects.get_or_create(
                                user=user,
                                content_type=content_type,
                                object_id=obj_id,
                                content=content_data
                            )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    args = {
        'bug': bug,
        'comments': comments,
        'comment_form': form,
    }
    return render(request, "bugdetail.html", args)


'''
A view which allows the user to report new bugs
'''
def report_bug(request):
    if request.method == "POST":
        new_bug_form = BugReportForm(request.POST)
        if new_bug_form.is_valid():
            form = new_bug_form.save(commit=False)
            form.reported_by = UserProfile.objects.get(user=request.user)
            form.save()
            return redirect('/bugs/')
        else:
            return redirect('/bugs/')
    else:
        new_bug_form = BugReportForm()
        args = {
            'new_bug_form': new_bug_form
        }
        return render(request, 'reportbug.html', args)
