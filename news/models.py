from django.db import models
from django.utils import timezone


'''
A piece of the News
'''
class New(models.Model):
    title = models.CharField(max_length=254, default="")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.title