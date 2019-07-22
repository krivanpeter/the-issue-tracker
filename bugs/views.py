from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from accounts.models import UserProfile
from comments.forms import CommentForm
from comments.models import Comment
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


