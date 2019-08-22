from django.conf.urls import url
from .views import all_features, feature_detail, upvote_feature


urlpatterns = [
    url(r'^$', all_features, name="features"),
    url(r'^(?P<slug>[-\w]+)/$', feature_detail, name="feature_detail"),
    url(r'^(?P<slug>[-\w]+)/upvote$', upvote_feature, name="upvote_feature"),
    ]