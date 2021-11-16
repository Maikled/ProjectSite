from django.shortcuts import render, HttpResponse
from Authentication.models import Admin, Manager, Employee
from Survey.views import list_of_Surveys
from Survey.models import Survey
from TaskMonitoring.views import check_user, index_TM, progress_of_ipr
from TaskMonitoring.models import IPR
import json


# Create your views here.
def index_PA(request, user):
    user_type = user.type
    if user_type == 'admin':
        user_data = Admin.objects.get(aut_id=user.id)
    elif user_type == 'manager':
        user_data = Manager.objects.get(aut_id=user.id)
    elif user_type == 'employee':
        user_data = Employee.objects.get(aut_id=user.id)
    else:
        user_data = None

    user_ipr = check_user(user.id)
    user_progress_of_ipr = progress_of_ipr(user.id)
    all_surveys = Survey.objects.all()
    all_employees = Employee.objects.all()

    return render(request, 'PersonalAccount/index_PA.html', {'user_type':user_type, 'user':user_data, 'user_ipr':user_ipr, 'progress_ipr':user_progress_of_ipr, 'all_surveys':all_surveys, 'all_employees':all_employees})


def redirect_to_list_of_Surveys(request):
    return list_of_Surveys(request)


def ipr(request):
    return index_TM(request)


def href(request):
    data = json.loads(request.body)
    task = IPR.objects.get(text_task=data)
    task.status = 'true'
    task.save()
    print(data)

    return HttpResponse(request)