from django.core.serializers import serialize
from django.http import JsonResponse
import json
import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from weasyprint import HTML
from . material_serializer import *
from . holidays import *

def calculate_diff(start, end):
    datetimeFormat = "%Y-%m-%d"
    weekday = 0
    weekend = []
    start_date = datetime.datetime.strptime(start, datetimeFormat)
    begin_date = datetime.datetime.strptime(start, datetimeFormat)
    end_date = datetime.datetime.strptime(end, datetimeFormat)
    while start_date < end_date:
        if start_date.weekday() not in [5,6] and start_date.strftime("%Y-%m-%d") not in holidays:
            
            weekday += 1
        start_date += datetime.timedelta(days=1)
    week_seconds = weekday * 60 * 60 *24
    diff = datetime.datetime.strptime(
		end, datetimeFormat) - datetime.datetime.strptime(start, datetimeFormat)
    context = {
        'weekday': weekday,
        'start_date': begin_date,
        'end_date': end_date,
    }
    return context


def leave_form_pdf(request):
    template_name = 'leave-form-pdf.html'
    diff = calculate_diff(request.GET.get('start_date'), request.GET.get('end_date'))
    print(diff)
    html_string = render_to_string(template_name, 
        {'start':diff.get('start_date'), 
        'end':diff.get('end_date'), 
        'description':request.GET.get('description'), 
        'days': int(diff.get('weekday')),
        'notes':request.GET.get('notes'), 
        'user':request.user})
    html = HTML(string = html_string)
    html.write_pdf(target='/tmp/leave_form.pdf', stylesheets=[ 
        'static/css/bs5.css',
        #  'static/css/report.css',
         'static/css/fontawesome.min.css'  
         ])
    fs = FileSystemStorage('/tmp')
    with fs.open('leave_form.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf', status=200)
        # response['Content-Disposition'] = f'attachment ; filename = "{user.first_name}_timesheet({start_date[5:]}_{end_date[5:]}).pdf"'
        response['Content-Disposition'] = f'attachment ; filename = "{request.user.first_name}_Application_leave_form.pdf"'
        # response['Location'] = 'timesheet:list'
        # print(response.status_code)
        # if response.status_code == 200:
        # 	messages.success(request, 'Your timesheet was saved!')
        return response


def get_leave_form(request):
    template_name = 'leave-form-pdf.html'
    if request.method == "POST":
        data = json.loads(request.body)
        diff = calculate_diff(data.get('start'), data.get('end'))

        html_string = render_to_string(template_name, {'start':data.get('start'), 'end':data.get('end'), 'description':data.get('description'), 'days': diff})
        html = HTML(string = html_string)
        html.write_pdf(target='/tmp/leave_form.pdf')
        fs = FileSystemStorage('/tmp')
        with fs.open('leave_form.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf', status=200)
         
            response['Content-Disposition'] = f'attachment ; filename = "teste.pdf"'
           
            return response
        
    return JsonResponse({"status":"error"})


def get_products(request):

    products = json.dumps(material)
    
    return JsonResponse(products.replace('\\',''), safe=False)