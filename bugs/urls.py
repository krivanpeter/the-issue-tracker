from django.conf.urls import url
from .views import all_bugs, bug_detail, report_bug


urlpatterns = [
    url(r'^$', all_bugs, name="bugs"),
    url(r'^(?P<pk>\d+)/$', bug_detail, name="bug_detail"),
    url(r'^bug-report/$', report_bug, name='report_bug'),
    ]