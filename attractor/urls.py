from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import (
    index, login_from_password_change,
    view_profile, edit_profile,
    change_password
)
from accounts import urls as urls_accounts
from news import urls as urls_news
from packages import urls as urls_packages
from bugs.views import report_bug
from features.views import report_feature
from comments.views import comment_delete
from bugs import urls as urls_bugs
from features import urls as urls_features
from cart import urls as urls_cart
from checkout import urls as urls_checkout
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
    url(r'^features/', include(urls_features)),
    url(r'^bugs/', include(urls_bugs)),
    url(r'^packages/', include(urls_packages)),
    url(r'^report-bug/$', report_bug, name='report_bug'),
    url(r'^report-feature/$', report_feature, name='report_feature'),
    url(r'^comment-delete/$', comment_delete, name='comment_delete'),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
