from django.db import models

# Create your models here.
class Survey(models.Model):
    survey_topic = models.CharField('survey_topic', max_length=250)

    def __str__(self):
        return self.survey_topic


class Question(models.Model):
    text_question = models.TextField('text_question', null=True, blank=True)
    question_topic = models.TextField('question_topic', null=True, blank=True)
    material_link = models.TextField('materials_link', null=True, blank=True)
    id_survey = models.ForeignKey('Survey', on_delete=models.CASCADE, null=True, blank=True)
    id_right_answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField('level', null=True)

    def __str__(self):
        return self.text_question


class Answer(models.Model):
    text_answer = models.TextField('text_answer')
    id_question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text_answer


class Log(models.Model):
    survey = models.TextField('survey', null=True, blank=True)
    user = models.TextField('user', null=True, blank=True)
    question = models.TextField('question', null=True, blank=True)
    answer = models.TextField('answer', null=True, blank=True)
    right_answer = models.TextField('right_answer', null=True, blank=True)
    level = models.IntegerField('level', null=True)

