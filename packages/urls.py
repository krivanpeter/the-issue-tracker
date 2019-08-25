from django.conf.urls import url
from .views import all_packages


urlpatterns = [
    url(r'^$', all_packages, name="all_packages"),
    ]