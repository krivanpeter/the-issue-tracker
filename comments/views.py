from django.http import HttpResponseRedirect, Http404
from .models import Comment


def comment_delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            obj = Comment.objects.get(id=id)
        except:
            raise Http404
        parent_obj_url = obj.content_object.get_absolute_url()
        if str(obj.user) != str(request.user):
            return HttpResponseRedirect(parent_obj_url)
        else:
            obj.delete()
        return HttpResponseRedirect(parent_obj_url)
    else:
        raise Http404()
