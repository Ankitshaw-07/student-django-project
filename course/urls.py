from django.urls import path
from .views import course_list, course_create

urlpatterns = [
    path('', course_list, name='course_list'),
    path('add/', course_create, name='course_add'),
]
