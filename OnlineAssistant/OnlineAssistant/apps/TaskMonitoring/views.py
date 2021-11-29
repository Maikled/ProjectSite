from django.shortcuts import render
from Survey.models import Log, Question
from .models import IPR
from Authentication.models import Employee

from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
import pdfkit

data_personal_task = {}

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
    # IPR.objects.filter(user_id=user_id).delete()
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
        statuses =  IPR.objects.raw(f'SELECT id, status FROM public."TaskMonitoring_ipr" ' + f"WHERE user_id='{user_id}' and topic_survey='{elem_survey.topic_survey}'")
        data[elem_survey.topic_survey] = round((sum([int(i.status) for i in statuses]) * 100) / len(statuses))

    return data


def index_TM(request):
    id_user = request.POST.get('id')
    survey = request.POST.get('data_key')
    tasks = {el.text_task:el.status for el in IPR.objects.filter(topic_survey=survey, user_id=id_user)}

    dict_of_task = {}
    t = 0
    f = 0
    for key, value in tasks.items():
        dict_of_task[key] = {el:value for el in Question.objects.filter(text_question=key)}
        f += 1
        if value == '1':
            t += 1

    return render(request, 'PersonalAccount/index_IPR.html', {'title':survey, 'tasks':dict_of_task, 'status_task':tasks, 'status':f'{t}/{f}'})


def personal_task(request):
    data_of_employee = request.POST.get('employee')

    data_of_employee = Employee.objects.get(aut_id=data_of_employee)
    ipr_of_employee = IPR.objects.filter(user_id=data_of_employee.id)

    position = ['Младший разработчик', 'Разработчик', 'Старший разработчик', 'Ведущий разработчик', 'Руководитель группы разработки']
    next_level = ''
    if data_of_employee.level < 5:
        next_level = f'{position[data_of_employee.level]} -> {position[data_of_employee.level+1]}'

    st = IPR.objects.raw(f'SELECT id, status FROM public."TaskMonitoring_ipr" ' + f"WHERE user_id='{data_of_employee.id}'")
    persent_finish = -1
    if st:
        persent_finish = (sum([int(i.status) for i in st]) * 100) / len(st)

    data_of_ipr = {}
    for el in ipr_of_employee:
        statuses = IPR.objects.raw(f'SELECT id, status FROM public."TaskMonitoring_ipr" ' + f"WHERE user_id='{data_of_employee.id}' and topic_survey='{el.topic_survey}'")
        count_finish = round((sum([int(i.status) for i in statuses]) * 100) / len(statuses))
        if el.topic_survey not in data_of_ipr:
            data_of_ipr[el.topic_survey] = {count_finish:[{el.text_task:el.status}]}
        else:
            data_of_ipr[el.topic_survey][count_finish].append({el.text_task:el.status})

    global data_personal_task
    data_personal_task = {'data_of_employee':data_of_employee, 'data_of_ipr':data_of_ipr, 'pretend':next_level, 'persent_finish':round(persent_finish)}
    return render(request, 'TaskMonitoring/index_personal_task.html', {'data_of_employee':data_of_employee, 'data_of_ipr':data_of_ipr, 'pretend':next_level, 'persent_finish':round(persent_finish)})


def create_PDF(request):
    global data_personal_task
    path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Место установки
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    html_template = render_to_string('TaskMonitoring/index_personal_task.html', data_personal_task)
    pdf = pdfkit.from_string(html_template, 'out.pdf', configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    return response

