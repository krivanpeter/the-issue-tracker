from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images', default='../media/profile_images/male_def.png')
    available_upvotes = models.PositiveIntegerField(default=0)
    country = CountryField(blank_label='(Select Country)', null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
