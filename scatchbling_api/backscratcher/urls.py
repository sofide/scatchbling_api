from django.urls import path, include

from backscratcher import views


urlpatterns = [
    path('api/', include('backscratcher.urls_api')),
    path('', views.home, name='home'),
    path('bs/<int:bs_pk>/', views.backscratcher_detail, name='bs_detail'),
]
