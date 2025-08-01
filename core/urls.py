from django.urls import path
from .views import UserViewSet, EntryViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'post': 'create'})),
    path('users/<int:pk>/', UserViewSet.as_view({'put': 'update'})),
    path('users/<int:pk>/delete/', UserViewSet.as_view({'delete': 'destroy'})),
    path('entries/', EntryViewSet.as_view({'post': 'create'})),
]
