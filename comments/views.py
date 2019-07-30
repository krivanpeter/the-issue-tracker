from accounts.models import UserProfile
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from .models import Comment


def create_comment(request, form):
    # A view which shows all the comments associated with the given object
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


def comment_delete(request, id):
    if request.method == "POST":
        obj = get_object_or_404(Comment, id=id)
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        return HttpResponseRedirect(parent_obj_url)
    else:
        raise Http404()
