from django.conf.urls import url
from .views import all_bugs, bug_detail, upvote_bug


urlpatterns = [
    url(r'^$', all_bugs, name="bugs"),
    url(r'^(?P<slug>[-\w]+)/$', bug_detail, name="bug_detail"),
    url(r'^(?P<slug>[-\w]+)/upvote$', upvote_bug, name="upvote_bug"),
    ]