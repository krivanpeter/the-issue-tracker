from django.conf.urls import url
from .views import all_news

urlpatterns = [
    url(r'^$', all_news, name="news"),
    ]