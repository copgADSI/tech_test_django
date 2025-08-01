from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Welcome to the Django API. Use /api/ for endpoints."})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', root_view),
]
