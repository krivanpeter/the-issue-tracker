from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from accounts.models import UserProfile
from comments.models import Comment

'''
A piece of Bug
'''
class Bug(models.Model):
    title = models.CharField(max_length=254, default="")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    upvotes = models.IntegerField(default=0)
    reported_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bug_detail", kwargs={"pk": self.pk})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

