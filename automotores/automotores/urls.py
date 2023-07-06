
from django.contrib import admin
from django.urls import path

from .views import AutosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", AutosView.as_view(), name = "Inicio")
    
]
