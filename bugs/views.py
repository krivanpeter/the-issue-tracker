from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from accounts.models import UserProfile
from comments.forms import CommentForm
from comments.views import create_comment
from .models import Bug, BugImages
from .forms import BugReportForm, BugImageForm


@login_required
def all_bugs(request):
    # A view which shows all the reported bugs
    if request.user.is_authenticated:
        bugs = Bug.objects.all()
        return render(request, "bugs.html", {"bugs": bugs})
    else:
        return redirect('index')


'''
A view which returns a single Bug object based on the ID(pk)
'''
def bug_detail(request, slug=None):
    if request.user.is_authenticated:
        bug = get_object_or_404(Bug, slug=slug)
        comments = bug.comments
        initial_data = {
            "content_type": bug.get_content_type,
            "object_id": bug.id
        }
        form = CommentForm(request.POST or None, initial=initial_data)
        create_comment(request, form)
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
        image_form_set = modelformset_factory(BugImages,
                                              form=BugImageForm, extra=3)
        if request.method == "POST":
            new_bug_form = BugReportForm(request.POST)
            bug_img_form = image_form_set(request.POST, request.FILES,
                                          queryset=BugImages.objects.none())

            if new_bug_form.is_valid() and bug_img_form.is_valid():
                bug_form = new_bug_form.save(commit=False)
                bug_form.reported_by = UserProfile.objects.get(user=request.user)
                bug_form.save()

                for form in bug_img_form.cleaned_data:
                    if form:
                        image = form['image']
                        photo = BugImages(bug=bug_form, image=image)
                        photo.save()

                return redirect('/bugs/')
            else:
                return redirect('/report-bug/')
        else:
            new_bug_form = BugReportForm()
            bug_img_form = image_form_set(queryset=BugImages.objects.none())
            args = {
                'new_bug_form': new_bug_form,
                'bug_img_form': bug_img_form
            }
            return render(request, 'reportbug.html', args)
    else:
        return redirect('index')


