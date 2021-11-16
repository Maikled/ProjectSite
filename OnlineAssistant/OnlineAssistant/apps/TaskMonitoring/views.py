from django.shortcuts import render
from Survey.models import Log, Question
from .models import IPR
import ast


# Create your views here.
def progress_of_ipr(user_id):
    data = IPR.objects.filter(user_id=user_id)

    if data:
        count_complited_tasks = 0
        for elem in data:
            if elem.status == '1':
                count_complited_tasks += 1

        return round((count_complited_tasks * 100) / len(data))

def check_user(user_id):
    data_surveys_of_user = Log.objects.filter(user=user_id)
    # IPR.objects.all().delete()

    for elem in data_surveys_of_user:
        data_ipr = IPR.objects.filter(user_id=user_id)
        data_text_tasks = [el.text_task for el in data_ipr]

        ipr = IPR()
        if elem.answer != elem.right_answer and elem.question not in data_text_tasks:
            ipr.user_id = user_id
            ipr.topic_survey = elem.survey
            ipr.text_task = elem.question
            ipr.status = '0'
            ipr.save()

    data = {}
    for elem_survey in IPR.objects.filter(user_id=user_id):
        data[elem_survey.topic_survey] = {el.text_task:el.status for el in IPR.objects.filter(topic_survey=elem_survey.topic_survey)}

    return data


def index_TM(request):
    id_user = request.POST.get('id')
    survey = request.POST.get('data_key')
    tasks = ast.literal_eval(request.POST.get('data_value'))
    print(tasks)

    dict_of_task = {}
    t = 0
    f = 0
    for key, value in tasks.items():
        dict_of_task[key] = {el:value for el in Question.objects.filter(text_question=key)}
        f += 1
        if value == '1':
            t += 1

    return render(request, 'PersonalAccount/index_IPR.html', {'title':survey, 'tasks':dict_of_task, 'status_task':tasks, 'status':f'{t}/{f}'})

