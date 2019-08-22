from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from accounts.models import UserProfile
from comments.forms import CommentForm
from comments.models import Comment
from .models import Feature
from .forms import FeatureReportForm



@login_required
def all_features(request):
    # A view which shows all the asked features,
    # ordered by the number of upvotes and the date of the report
    if request.user.is_authenticated:
        bug_list = Feature.objects.annotate(count=Count('upvotes')).order_by('-count')
        page = request.GET.get('page', 1)
        paginator = Paginator(bug_list, 10)
        try:
            features = paginator.page(page)
        except PageNotAnInteger:
            features = paginator.page(1)
        except EmptyPage:
            features = paginator.page(paginator.num_pages)
        return render(request, "features.html", {"features": features})
    else:
        return redirect('index')


def feature_detail(request, slug=None):
    # A view which returns a single Bug object based on the ID(pk)
    if request.user.is_authenticated:
        feature = get_object_or_404(Feature, slug=slug)
        comments = feature.comments
        initial_data = {
            "content_type": feature.get_content_type,
            "object_id": feature.id
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
            'feature': feature,
            'comments': comments,
            'comment_form': form,
        }
        return render(request, "featuredetail.html", args)
    else:
        return redirect('index')


def report_feature(request):
    # A view which allows the user to ask new features
    if request.user.is_authenticated:
        if request.method == "POST":
            new_feature_form = FeatureReportForm(request.POST)

            if new_feature_form.is_valid():
                feature_form = new_feature_form.save(commit=False)
                feature_form.reported_by = UserProfile.objects.get(user=request.user)
                feature_form.save()
                return redirect('/features/')
            else:
                data = {'is_valid': False}
                return JsonResponse(data)
        else:
            new_feature_form = FeatureReportForm()
            args = {
                'new_feature_form': new_feature_form,
            }
            return render(request, 'reportfeature.html', args)
    else:
        return redirect('index')


def upvote_feature(request, slug=None):
    # A view which allows the user to like and unlike features
    if request.user.is_authenticated:
        data = {'user_upvoted': False}
        feature = get_object_or_404(Feature, slug=slug)
        user = request.user
        if user.is_authenticated():
            if user in feature.upvotes.all():
                feature.upvotes.remove(user)
                data['user_upvoted'] = False
            else:
                feature.upvotes.add(user)
                data['user_upvoted'] = True
        return JsonResponse(data)
    else:
        return redirect('index')