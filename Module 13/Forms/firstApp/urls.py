from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='homepage'),
    path('about/', views.about , name='aboutpage'),
    path('form/', views.form , name='form'),
    # path('django_form/', views.DjangoForm , name='django_form'),
    path('django_form/', views.passworsValidation , name='django_form'),
]