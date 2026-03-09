from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("competences/", include("competences.urls")),
    path('admin/', admin.site.urls),
]
