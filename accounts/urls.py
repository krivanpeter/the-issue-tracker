from django.conf.urls import url, include
from . import urls_reset
from .views import register, logout, login, check_username, check_email, check_userdata


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^check_username/$', check_username, name='check_username'),
    url(r'^check_email/$', check_email, name='check_email'),
    url(r'^check_userdata/$', check_userdata, name='check_userdata'),
]
