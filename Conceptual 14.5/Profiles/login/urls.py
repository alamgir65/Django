
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='Home'),
    path('form/', views.StuForm , name='Form'),
    path('django_form/' , views.DjangoForm , name='DjangoForms'),
    
]