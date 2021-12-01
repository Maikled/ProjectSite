from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
import pdfkit
import datetime
import os
from django.http import FileResponse

# Create your views here.
def create_PDF(request, data):
    data['date'] = datetime.date.today()
    data['time'] = datetime.datetime.now().strftime("%H:%M:%S")

    path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Место установки
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    html_template = render_to_string('Automation/index_report.html', data)
    pdfkit.from_string(html_template, 'report.pdf', configuration=config)

    file = open('report.pdf', 'rb')
    return FileResponse(file, content_type='application/pdf')

    # return render(request, 'Automation/index_report.html', data)