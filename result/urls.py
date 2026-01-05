from django.urls import path
from .views import result_list, result_create

urlpatterns = [
    path('', result_list, name='result_list'),
    path('add/', result_create, name='result_add'),
]
