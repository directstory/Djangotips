from django.urls import path

from userRole.views import mtom

urlpatterns = [
    path('mtom', mtom)
]