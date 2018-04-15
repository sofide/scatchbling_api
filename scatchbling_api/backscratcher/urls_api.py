from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from backscratcher import views


urlpatterns = [
    url(r'^api/$', views.BackscratcherList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.BackscratcherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
