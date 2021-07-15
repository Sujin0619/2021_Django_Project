from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('food/<str:pk>/', views.detail)
]
