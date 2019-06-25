from django.conf.urls import url
from .views import all_bugs, report_bug


urlpatterns = [
    url(r'^$', all_bugs, name="bugs"),
    url(r'^bug-report/$', report_bug, name='report_bug'),
    ]