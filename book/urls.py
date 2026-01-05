from django.urls import path
from .views import book_list, book_create

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', book_create, name='book_add'),
]
