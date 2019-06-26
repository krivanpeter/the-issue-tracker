from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from accounts.models import UserProfile
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
    content_type = ContentType.objects.get_for_model(Bug)
    obj_id = bug.id
    comments = Comment.objects.filter(content_type=content_type, object_id=obj_id)
    args = {
        'bug': bug,
        'comments': comments,
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
        new_bug_from = BugReportForm()
        args = {
            'new_bug_from': new_bug_from
        }
        return render(request, 'reportbug.html', args)
