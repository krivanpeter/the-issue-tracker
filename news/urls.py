from django.conf.urls import url
from .views import all_news, new_detail, create_new

urlpatterns = [
    url(r'^$', all_news, name="news"),
    url(r'^(?P<pk>[-\w]+)/$', new_detail, name="new_detail"),
    url(r'^create-new/$', create_new, name='create_new'),
    ]