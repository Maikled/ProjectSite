from django.urls import path
from . import views

urlpatterns = [
    path('create_PDF', views.create_PDF, name='create_PDF'),
]