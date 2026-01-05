from django.urls import path
from .views import department_list, department_create

urlpatterns = [
    path('', department_list, name='department_list'),
    path('add/', department_create, name='department_add'),
]
