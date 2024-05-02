
from django.urls import path
from . import views

urlpatterns = [
    path('add_profile/', views.add_profiles, name='add_profile'),
]