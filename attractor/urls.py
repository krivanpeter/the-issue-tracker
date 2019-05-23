from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index, login_from_password_change
from accounts import urls as urls_accounts
from news import urls as urls_news
from bugs import urls as urls_bugs
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^index/$', login_from_password_change, name="login_from_password_change"),
    url(r'^news/', include(urls_news)),
    url(r'^bugs/', include(urls_bugs)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
