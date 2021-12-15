from django.urls import path, include
from . import views

urlpatterns = [
    path('index_Survey', views.index_Survey, name='index_Survey'),
    path('reply', views.reply, name='reply'),
    path('index_end_Survey', views.index_end_Survey, name='index_end_Survey'),
    path('back_to_PA', views.back_to_PA, name='back_to_PA'),
    path('save_Survey', views.save_Survey, name='save_Survey'),
    path('index_end_editor', views.index_end_editor, name='index_end_editor'),
    path('delete_question', views.delete_question, name='delete_question'),
    path('delete_survey', views.delete_survey, name='delete_survey'),
]