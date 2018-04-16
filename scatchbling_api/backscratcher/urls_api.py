from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as token_views

from backscratcher import views_api as views


urlpatterns = [
    url(r'^$', views.BackscratcherList.as_view()),
    url(r'^(?P<pk>[0-9]+)/?$', views.BackscratcherDetail.as_view()),
    url(r'^api-token-auth/', token_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
