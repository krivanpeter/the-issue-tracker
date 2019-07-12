from django.conf.urls import url
from .views import all_bugs, bug_detail


urlpatterns = [
    url(r'^$', all_bugs, name="bugs"),
    url(r'^(?P<slug>[-\w]+)/$', bug_detail, name="bug_detail"),
    ]