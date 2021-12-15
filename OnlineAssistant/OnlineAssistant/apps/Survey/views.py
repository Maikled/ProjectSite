from django.shortcuts import render, HttpResponse, redirect
from .models import Survey, Question, Answer, Log
from Authentication.models import Authentication, Employee
import PersonalAccount
from json import loads

# Create your views here.


def list_of_Surveys(request):
    user_id = request.POST.get('id')
    user = Employee.objects.get(aut_id=user_id)

    data_Surveys = Survey.objects.all()
    surveys = []
    for el in data_Surveys:
        if Question.objects.filter(id_survey=el.id, level=user.level+1):
            surveys.append(el)

    data_Log = Log.objects.filter(user=user_id)
    user_logs = []
    for el in data_Log:
        user_logs.append(el.survey)

    return render(request, 'Survey/index_list_of_Surveys.html', {'data_Surveys':surveys, 'user_id':user_id, 'user_logs':user_logs, 'level':user.level})


def index_Survey(request):
    survey_id = request.GET.get('id_Survey')
    user_id = request.GET.get('user_id')
    user_level = request.GET.get('level')
    data_Survey = Survey.objects.get(id=survey_id)
    data_Question = Question.objects.filter(id_survey_id=data_Survey.id, level=(int(user_level)+1))

    data = {}
    data_right_answer = {}
    for question in data_Question:
        data[question] = Answer.objects.filter(id_question_id=question.id)
        data_right_answer[question] = question.id_right_answer

    return render(request, 'Survey/index_Survey.html', {'title_Survey':data_Survey, 'data':data, 'right_answers':data_right_answer, 'survey':data_Survey, 'user':user_id, 'level':user_level})


def reply(request):
    data = loads(request.body)
    # Log.objects.all().delete()
    for key in data:
        question_id = key
        question = Question.objects.get(id=question_id)
        fields = loads(data.get(key))
        answer = fields.get('answer')
        survey = fields.get('survey')
        user_id = fields.get('user')
        user_level = fields.get('level')
        right_answer = fields.get('right_answer')

        log = Log()
        log.survey = survey
        log.user = user_id
        log.question = question.text_question
        log.answer = answer
        log.right_answer = right_answer
        log.level = int(user_level)
        log.save()

    return HttpResponse(request)


def index_end_Survey(request):
    user_id = request.POST.get('user')
    return render(request, 'Survey/index_end_Survey.html', {'user_id':user_id})


def back_to_PA(request):
    user_id = request.POST.get('user')
    authentication_user = Authentication.objects.get(id=user_id)
    return PersonalAccount.views.index_PA(request, authentication_user)


def editor_of_survey(request):
    user = request.GET.get('user_id')
    data = {}

    id_survey = request.GET.get('id_Survey')
    if id_survey:
        survey = Survey.objects.get(id=id_survey)
        data['survey_name'] = survey.survey_topic

        questions = Question.objects.filter(id_survey_id=survey.id)
        data['questions'] = {}

        for question in questions:
            data['questions'][question] = Answer.objects.filter(id_question_id=question.id)
    else:
        data['survey_name'] = ""
        data['questions'] = {}
        data['questions'][""] = ["", "", "", ""]

    return render(request, 'Survey/index_editor.html', {'data':data, 'user':user})

def save_Survey(request):
    data = loads(request.body)
    survey_name = data['survey_name']
    try:
        survey = Survey.objects.get(survey_topic=survey_name)
    except:
        survey = Survey()

    survey.survey_topic = survey_name
    survey.save()

    for key_question, value_question in data['data'].items():
        question = Question()
        text_of_question = key_question
        question.text_question = text_of_question
        question.id_survey = survey
        question.save()

        for key_answer, value_answer in value_question['answers'].items():
            answer = Answer()
            answer_text = key_answer
            answer.text_answer = answer_text
            answer.id_question = question
            answer.save()
            if value_answer == True:
                question.id_right_answer = answer

        for key_info, value_info in value_question['info'].items():
            question.question_topic = key_info
            question.material_link = value_info

        question.level = int(value_question['level'])
        question.save()

    return HttpResponse(request)


def index_end_editor(request):
    user = request.POST.get('user')
    return render(request, 'Survey/index_end_editor.html', {'user_id':user})


def delete_question(request):
    data = loads(request.body)
    question = data['question']
    question = Question.objects.get(text_question=question)
    answers = Answer.objects.filter(id_question=question.id)
    for i in answers:
        i.delete()
    question.delete()

    return HttpResponse(request)


def delete_survey(request):
    data = loads(request.body)
    survey = data['survey_name']
    survey = Survey.objects.filter(survey_topic=survey)
    for i in survey:
        i.delete()

    return HttpResponse(request)