from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EntryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'entries', EntryViewSet, basename='entry')

urlpatterns = [
    path('', include(router.urls)),
]
