from django.urls import path

from . import views

app_name = "competences"

urlpatterns = [
    path("", views.index, name="index"),
]