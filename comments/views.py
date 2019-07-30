from accounts.models import UserProfile
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from .models import Comment


def comment_delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        obj = get_object_or_404(Comment, id=id)
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        return HttpResponseRedirect(parent_obj_url)
    else:
        raise Http404()
