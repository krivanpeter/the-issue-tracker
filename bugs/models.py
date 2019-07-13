from accounts.models import UserProfile
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify


class Bug(models.Model):
    # A piece of Bug
    title = models.CharField(max_length=60, default="")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    upvotes = models.IntegerField(default=0)
    reported_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-upvotes']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bug_detail", kwargs={"slug": self.slug})

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


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Bug.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_bug_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


class BugImages(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='images', default="None")
    image = models.ImageField(upload_to="bugs_images", null=True, blank=True)

    def __str__(self):
        return str(self.bug.id)


pre_save.connect(pre_save_bug_receiver, sender=Bug)