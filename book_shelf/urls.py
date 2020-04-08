from django.urls import path
from . import views

urlpatterns = [
    path('', views.shelf_itself, name='shelf_itself'),
]
