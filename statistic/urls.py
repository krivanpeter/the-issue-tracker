from django.conf.urls import url
from .views import all_data


urlpatterns = [
    url(r'^$', all_data, name="all_data"),
]