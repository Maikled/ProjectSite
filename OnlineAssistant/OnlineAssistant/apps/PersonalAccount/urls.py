from django.urls import path, include
from Survey.views import index_Survey
from . import views

urlpatterns = [
    path('', views.index_PA, name='index_PA'),
    path('list_of_Surveys', views.redirect_to_list_of_Surveys, name='list_of_Surveys'),
    path('ipr', views.ipr, name='ipr'),
    path('href', views.href, name='href'),
    path('index_Survey', index_Survey, name='index_Survey'),
    path('personal_task', views.personal_task_of_employes, name='personal_task'),
]