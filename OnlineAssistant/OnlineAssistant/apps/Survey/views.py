from django.shortcuts import render, HttpResponse
from .models import Survey, Question, Answer, Log
from Authentication.models import Authentication
import PersonalAccount
from json import loads

# Create your views here.


def list_of_Surveys(request):
    user_id = request.POST.get('id')
    data_Surveys = Survey.objects.all()
    data_Log = Log.objects.filter(user=user_id)

    user_logs = []
    for el in data_Log:
        user_logs.append(el.survey)

    return render(request, 'Survey/index_list_of_Surveys.html', {'data_Surveys':data_Surveys, 'user':user_id, 'user_logs':user_logs})


def index_Survey(request):
    survey_id = request.GET.get('id_Survey')
    user = request.GET.get('user')
    data_Survey = Survey.objects.get(id=survey_id)
    data_Question = Question.objects.filter(id_survey_id=data_Survey.id)

    data = {}
    data_right_answer = {}
    for question in data_Question:
        data[question] = Answer.objects.filter(id_question_id=question.id)
        data_right_answer[question] = question.id_right_answer

    return render(request, 'Survey/index_Survey.html', {'title_Survey':data_Survey, 'data':[data], 'right_answers':data_right_answer, 'survey':data_Survey, 'user':user})


def reply(request):
    data = loads(request.body)
    # Log.objects.all().delete()
    for key in data:
        question = key
        fields = loads(data.get(key))
        answer = fields.get('answer')
        survey = fields.get('survey')
        user_id = fields.get('user')
        right_answer = fields.get('right_answer')

        log = Log()
        log.survey = survey
        log.user = user_id
        log.question = question
        log.answer = answer
        log.right_answer = right_answer
        log.save()

    return HttpResponse(request)


def index_end_Survey(request):
    user_id = request.POST.get('user')
    return render(request, 'Survey/index_end_Survey.html', {'user_id':user_id})


def back_to_PA(request):
    user_id = request.POST.get('user')
    authentication_user = Authentication.objects.get(id=user_id)
    return PersonalAccount.views.index_PA(request, authentication_user)