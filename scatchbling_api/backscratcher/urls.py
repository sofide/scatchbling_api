from django.urls import path, include

from backscratcher import views


urlpatterns = [
    path('api/', include('backscratcher.urls_api')),
    path('', views.home)
]
