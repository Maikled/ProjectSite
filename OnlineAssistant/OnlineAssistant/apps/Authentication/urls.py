from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('verification', views.verification, name = "verification")
]