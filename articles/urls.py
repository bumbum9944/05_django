from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new),
    path('create/', views.new),
    # Read
    path('', views.index),
]
