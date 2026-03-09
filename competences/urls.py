from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "competences"

urlpatterns = [
    path("", views.index, name="index"),
    path('skills/', views.skills, name='skills'),
    path('add/', views.add_slot, name='add'),
    path('search/', views.search, name='search'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]