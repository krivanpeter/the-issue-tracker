from django.db import models
from django.utils import timezone
from accounts.models import UserProfile

'''
A piece of Bug
'''
class Bug(models.Model):
    title = models.CharField(max_length=254, default="")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    reported_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

