from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('floyd_warshall.urls')),
    path('admin/', admin.site.urls),
]
