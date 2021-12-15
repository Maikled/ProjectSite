from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Authentication
from PersonalAccount.views import index_PA


# Create your views here.
def index(request):
    return render(request, 'Authentication/index.html', {'status':None})


def verification(request):
    login = request.POST.get('login')
    password = request.POST.get('password')

    try:
        authentication_user = Authentication.objects.get(login=login, password=password)
        return index_PA(request, authentication_user)
    except:
        return render(request, 'Authentication/index.html', {'status': 'false'})

