from django.urls import path, include

urlpatterns = [
    path('api/', include('backscratcher.urls_api')),
]
