from django.db import models

# Create your models here.
class IPR(models.Model):
    user_id = models.CharField('user_id', max_length=50)
    text_task = models.TextField('text_task')
    status = models.IntegerField('status')
    topic_survey = models.CharField('topic_survey', max_length=50)