from django.urls import path  # type: ignore
from django.contrib.auth import views as auth_views  # type: ignore

from . import views

app_name = "competences"

urlpatterns = [
    path("", views.index, name="index"),
    path('skills/', views.skills, name='skills'),
    path('add/', views.add_slot, name='add'),
    path('available/', views.available, name='available'),
    path('search/', views.search, name='search'),
    path('search_available_slots/', views.search_available_slots, name='search_available_slots'),
    path('purpose_help/<int:slot_id>/', views.purpose_help, name='purpose_help'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
