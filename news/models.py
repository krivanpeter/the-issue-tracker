from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment


class New(models.Model):
    # A piece of the News
    title = models.CharField(max_length=254, default="")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="news_images", blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("new_detail", kwargs={"pk": self.pk})

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