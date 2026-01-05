from django.urls import path
from .views import subject_list, subject_create

urlpatterns = [
    path('', subject_list, name='subject_list'),
    path('add/', subject_create, name='subject_add'),
]
