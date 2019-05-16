from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, logout, login, check_username, check_email

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^check_username/$', check_username, name='check_username'),
    url(r'^check_email/$', check_email, name='check_email'),
]
