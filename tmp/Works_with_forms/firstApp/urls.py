
from django.urls import path
from .views import home
urlpatterns = [
    # path('', views.index , name='Homepage'),
    path('', home , name='Homepage'),
    # path('delete/<int:roll>' , views.student_delete , name='Delete_Student'),
]