from django.conf.urls import url
from .views import all_news, new_detail

urlpatterns = [
    url(r'^$', all_news, name="news"),
    url(r'^(?P<pk>\d+)/$', new_detail, name="new_detail")
    ]