from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import (
    index, login_from_password_change,
    view_profile, edit_profile,
    change_password
)
from accounts import urls as urls_accounts
from news import urls as urls_news
from bugs.views import report_bug
from comments.views import comment_delete
from bugs import urls as urls_bugs
from django.views import static
from .settings import MEDIA_ROOT

admin.site.site_header = "Unicorn Attractor Administration"
admin.site.site_title = "Unicorn Attractor Administration"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^super-secret/admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^profile/(?P<username>.+)/$', view_profile, name='view_profile'),
    url(r'^profile/edit$', edit_profile, name='edit_profile'),
    url(r'^change-password/$', change_password, name='change_password'),
    url(r'^index/$', login_from_password_change, name="login_from_password_change"),
    url(r'^news/', include(urls_news)),
    url(r'^report-bug/$', report_bug, name='report_bug'),
    url(r'^bugs/', include(urls_bugs)),
    url(r'^comment-delete/$', comment_delete, name='comment_delete'),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
