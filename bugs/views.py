from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from .models import Bug
from .forms import BugReportForm


@login_required
def all_bugs(request):
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})


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
