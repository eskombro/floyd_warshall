from django.urls import path
from .views import handle_auth, handle_logout, home, floyd_warshall

urlpatterns = [
    path('', home),
    path('logout', handle_logout),
    path('authenticate', handle_auth),
    path('floyd-warshall', floyd_warshall),
]
