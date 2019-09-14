from django.conf.urls import url
from .views import statistic, ChartData


urlpatterns = [
    url(r'^$', statistic, name="statistic"),
    url(r'^api/chart/data/$', ChartData.as_view()),
]
