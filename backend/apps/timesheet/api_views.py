from urllib import response
from django.core import serializers
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import json
import datetime
from datetime import  date
from weasyprint import HTML

from backend.apps.timesheet.serializers import TimesheetSerializer
from .models import Timesheet
from backend.apps.job.models import JobNumber
from backend.apps.mjs.models import MjsNumber
from backend.apps.account.models import UserProfile
from backend.apps.core.qs_sum_time import total_time, sum_mjs, convert_seconds, sum_mjs_api

from backend.apps.core.qs_sum_time import *


DAYS_OFF = [
			'Sick Leave', 
			'Covid Lockdown', 
			'Public Holiday', 
			'ACC Leave', 
			'Leave Without Pay', 
			'Annual Leave', 
			'Bereavement Leave', 
			'Parental Leave', 
			'Domestic Leave']


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet(request,page):
    if not request.user.is_authenticated:
        return
    timesheet = Timesheet.objects.filter(user = request.user).order_by('-date', 'time_in')
    paginator = Paginator(timesheet, 20)
    page_obj = paginator.get_page(page)
    serializer = TimesheetSerializer(page_obj, many=True)
    return Response({'data':serializer.data, 'calculatedHours':'','hasNext':page_obj.has_next()})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet_search(request):
    total = datetime.timedelta(0)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    days_off_only = request.GET.get('days_off_only')
    custom_filter = request.GET.get('custom_filter')
    timesheet = Timesheet.objects.filter(
            Q(user = request.user)&
			Q(date__gte=start_date)&
			Q(date__lte=end_date)).order_by('date', 'time_in')
    serializer = TimesheetSerializer(timesheet, many = True)
    total = total_time(calc_time(timesheet))
    
    # return JsonResponse({'data':serializer.data, 'calculatedHours':total}, safe = False, status = 200)
    return Response({'data':serializer.data, 'calculatedHours':total})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_timesheet_calendar_range(request, format=None):
    month = request.GET.get('month')
    year = request.GET.get('year')
    timesheet = Timesheet.objects.filter(Q(user = request.user)&Q(date__month=month)&Q(date__year=year))
    serializer = TimesheetSerializer(timesheet, many = True)
    return Response(serializer.data)
        
      
def get_timesheet_calendar_modal(request):
    date = request.GET.get('date')
   
    timesheet = Timesheet.objects.filter(Q(user = request.user)&Q(date=date))
    serializer = TimesheetSerializer(timesheet, many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_timesheet(request):
    if request.method == 'POST':
        data  = request.data
        print(data)
        mjs_number = MjsNumber.objects.get(pk=data.get('mjs').get('id'))
        if mjs_number.user != request.user:
            raise Http404

        job_number = JobNumber.objects.get(pk = mjs_number.mjs_job.id)
        client = job_number.job_client.client_name
        supervisor = job_number.job_supervisor.supervisor_name
        address = job_number.job_address
        start_date = datetime.datetime.strptime(data.get('data').get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(data.get('data').get('end_date'), '%Y-%m-%d').date()

        description = data.get('data').get('description')
        if not description:
            description = mjs_number.mjs_description
        time_in = data.get('data').get('time_in')
        time_out = data.get('data').get('time_out')
        
        break_time = data.get('data').get('break_time')
        ts_data = {
            'user': request.user,
            'mjs': mjs_number,
            'job': job_number,
            'client': client,
            'address': address,
            'description': description,
            'time_in': time_in,
            'time_out': time_out,
            'break_time': break_time,
            'supervisor': supervisor,
            'date':start_date
        }
        # ts = Timesheet.objects.create(**ts_data)
        # ts.save()
        rows = 1
        if start_date < end_date:
            
            rows = 0
            while start_date <= end_date:
               
                ts_data['date'] = start_date
                timesheet_validator_pwa(request, ts_data)
                start_date = start_date + datetime.timedelta(days=1)
                rows += 1
        else:
            ts_data['date'] = start_date
            timesheet_validator_pwa(request, ts_data)
        return JsonResponse({'status':'success', 'rows':rows})
    return JsonResponse({'status':'ok'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def timesheet_edit(request, pk):
    obj = Timesheet.objects.get(pk = pk)
    sec_before = obj.seconds
    mjs_job = obj.mjs.mjs_job.id
    job = JobNumber.objects.get(pk=mjs_job)

    if request.method == 'POST':
        data = request.data.get('data')
        time_in = convert_or_create_last_second_digits(data.get('time_in'))
        time_out = convert_or_create_last_second_digits(data.get('time_out'))

        date = data.get('start_date')
        description = data.get('description')
        break_time = data.get('break_time')
        print(date)

        obj.time_in = obj.time_in if not time_in else time_in
        obj.date = date
        obj.time_out = obj.time_out if not time_out else time_out
        obj.date = obj.date if not date else date
        obj.description =  obj.description if not description else description 
        obj.break_time = break_time

        if not obj.description:
            return JsonResponse({'status':'400','message':'All fields must be filled'})
        if not obj.mjs.mjs_hours:
          
            hour = edit_sum_mjs_api(obj.time_in, obj.time_out, obj.break_time)
            obj.mjs.mjs_hours = str(convert_seconds(hour.seconds))[:5]
            obj.mjs.mjs_seconds = hour.seconds
            obj.seconds = hour.seconds
            obj.mjs.save()

        else:
            hours = edit_sum_mjs_api(obj.time_in, obj.time_out, obj.break_time)
            seconds = hours.seconds
            obj.seconds = seconds
            
            seconds_from_mjs = obj.mjs.mjs_seconds
            seconds += seconds_from_mjs
            obj.mjs.mjs_seconds = seconds
            
            obj.mjs.mjs_hours = (str(total_time(datetime.timedelta(seconds=seconds))))
            obj.mjs.save()
        
        if not job.job_hours:
            hour = edit_sum_mjs_api(obj.time_in, obj.time_out, obj.break_time)
            job.job_hours = convert_seconds(hour.seconds)
            job.job_seconds = hour.seconds
            job.save()

        else:
            hours = edit_sum_mjs_api(obj.time_in, obj.time_out, obj.break_time)
            seconds = hours.seconds
            
            seconds_from_mjs = job.job_seconds
            seconds += seconds_from_mjs
            job.job_seconds = seconds
            
            job.job_hours = (str(total_time(datetime.timedelta(seconds=seconds))))
            job.save()
			
            # Remove the seconds from daywork before edit and save with new seconds
            obj.mjs.mjs_seconds -= sec_before
            obj.mjs.mjs_hours = (str(total_time(datetime.timedelta(seconds=obj.mjs.mjs_seconds))))
            obj.mjs.save()
            job.job_seconds -= sec_before
            job.job_hours = (str(total_time(datetime.timedelta(seconds=job.job_seconds))))
            job.save()
            obj.save()
            return JsonResponse({'status':'200','message':'Your day work was updated with success'})

    
    return JsonResponse({'status':'400','message':'All fields must be filled'})



def timesheet_validator_pwa(request, obj):
    data = Timesheet(user =request.user,
        date = obj['date'],
        client = obj['client'],
        address = obj['address'],
        job = obj['job'],
        mjs = obj['mjs'],
        description = obj['description'],
        time_in = obj['time_in'],
        time_out = obj['time_out'],
        break_time = obj['break_time'],
        supervisor = obj['supervisor'])

    mjs = data.mjs
    job = data.job
    if not mjs.mjs_hours:
        hour = sum_mjs_api(data.time_in, data.time_out, data.break_time)
        mjs.mjs_hours = str(convert_seconds(hour.seconds))[:5]
        mjs.mjs_seconds = hour.seconds
        data.seconds = hour.seconds
        mjs.save()
        
    else:
        hours = sum_mjs_api(data.time_in, data.time_out, data.break_time)
        seconds = hours.seconds
        data.seconds = seconds
        
        seconds_from_mjs = mjs.mjs_seconds
        seconds += seconds_from_mjs
        mjs.mjs_seconds = seconds
        
        mjs.mjs_hours = (str(total_time(datetime.timedelta(seconds=seconds))))
        mjs.save()
    
    if not job.job_hours:
        hour = sum_mjs_api(data.time_in, data.time_out, data.break_time)
        job.job_hours = convert_seconds(hour.seconds)
        job.job_seconds = hour.seconds
        job.save()
        
    else:
        hours = sum_mjs_api(data.time_in, data.time_out, data.break_time)
        seconds = hours.seconds
        
        seconds_from_mjs = job.job_seconds
        seconds += seconds_from_mjs
        job.job_seconds = seconds
        
        job.job_hours = (str(total_time(datetime.timedelta(seconds=seconds))))
        job.save()
    
        data.save()
        return JsonResponse({'status':'success'})




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def timesheet_delete(request):
    if request.method == "POST":
        data = request.data
        ts_list = data.get('ts')
        for item in ts_list:
            ts = Timesheet.objects.get(pk = item)
            
            if ts.user != request.user:
               return JsonResponse({},status = 400)
            if not ts.seconds:
                ts.delete()
            else:
                job = JobNumber.objects.get(pk = ts.job.id)
                mjs = MjsNumber.objects.get(pk =  ts.mjs.id)
                mjs.mjs_seconds -= ts.seconds
                mjs.mjs_hours = (str(total_time(datetime.timedelta(seconds=mjs.mjs_seconds))))
                mjs.save()
                job.job_seconds -= ts.seconds
                job.job_hours = (str(total_time(datetime.timedelta(seconds=job.job_seconds))))
                job.save()
                ts.delete()
        return JsonResponse({'status':'200','message':f'{len(ts_list)} {"rows were" if len(ts_list) > 1 else "row was"}  delete with success'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def timesheet_export(request):
	start_date = request.GET.get('start_date')
	end_date = request.GET.get('end_date')

	#####
	days_off_only = request.GET.get('days_off_only')
	
	custom_filter = request.GET.get('custom_filter')

	######
	user = request.user
	template_name = 'timesheet_pdf2.html'
	total = datetime.timedelta()
	user_profile = get_object_or_404(UserProfile, user = user)

	# if not user_profile.user_email_destiny:
	# 	messages.error(request, 'Please, fill your profile before export')
	# 	return redirect('accounts:update')
	

	obj = Timesheet.objects.order_by('date','time_in').filter(
		Q(user = request.user)&
		Q(date__gte = start_date)&
		Q(date__lte = end_date))
	
	#######

	if not custom_filter:
			obj = obj.filter(
				Q(user = request.user)&
				Q(date__gte=start_date)&
				Q(date__lte=end_date)).order_by('date','time_in')
			
	if custom_filter and not days_off_only:
		obj = obj.filter(
		Q(user = request.user)&
		Q(date__gte=start_date)&
		Q(date__lte=end_date))
		obj = obj.filter(
			Q(description__icontains=custom_filter) |
			Q(client__icontains=custom_filter)|
			Q(address__icontains=custom_filter)|
			Q(job__job_number__icontains=custom_filter)|
			Q(supervisor__icontains=custom_filter)|
			Q(mjs__mjs_number__icontains=custom_filter)).order_by('date')
		
		
	if days_off_only:
		obj = obj.filter(
			Q(user = request.user)&
			Q(date__gte=start_date)&
			Q(date__lte=end_date)&
			Q(description__in=DAYS_OFF)).order_by('date')
		
	######

	total = calc_time(obj)
	horas = total_time(total)
	html_string = render_to_string(template_name,{'obj':obj, 'user':user, 'total':horas,'user_profile':user_profile, 'timesheet_number':str(obj.last().id).zfill(6) })
	html = HTML(string = html_string)
	
	html.write_pdf(target='/tmp/timesheet.pdf', stylesheets=[ 
        # 'static/css/bs5.css',
        #  'static/css/report.css',
        #  'static/css/fontawesome.min.css'  
         ])
	
	
	fs = FileSystemStorage('/tmp')
	with fs.open('timesheet.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf', status=200)
		response['Content-Disposition'] = f'attachment ; filename = "{user.first_name}_timesheet({start_date[5:]}_{end_date[5:]}).pdf"'
		response['Location'] = 'timesheet:list'
		# print(response.status_code)
		# if response.status_code == 200:
		# 	messages.success(request, 'Your timesheet was saved!')
		return response

def timesheet_send(request):
    data = date.today()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    email_addressee = request.GET.get('email')
    
	#####
    days_off_only = request.GET.get('days_off_only')
    custom_filter = request.GET.get('custom_filter')

	######
    user = request.user
    template_name = 'timesheet_pdf2.html'
    total = datetime.timedelta()
    user_profile = UserProfile.objects.get(user =request.user)
    email = user_profile.user_email_destiny
    if email_addressee:
        email = email_addressee
    # try:
    # 	user_profile = UserProfile.objects.get(user =request.user)
    # 	if not user_profile.user_email_destiny:
    # 		messages.error(request,'You need to set a email to send your timesheet')
    # 		return redirect('accounts:update')
    # except:
    # 	messages.error(request,'You need to add your company name and your position first before send your timesheet')
    # 	return redirect('accounts:add')

    obj = Timesheet.objects.order_by('date','time_in').filter(
		Q(user = request.user)&
		Q(date__gte = start_date)&
		Q(date__lte = end_date))

	#######
	
    if not custom_filter:
            obj = obj.filter(
				Q(user = request.user)&
				Q(date__gte=start_date)&
				Q(date__lte=end_date)).order_by('date','time_in')
			
    if custom_filter and not days_off_only:
        obj = obj.filter(
		Q(user = request.user)&
		Q(date__gte=start_date)&
		Q(date__lte=end_date))
        obj = obj.filter(
			Q(description__icontains=custom_filter) |
			Q(client__icontains=custom_filter)|
			Q(address__icontains=custom_filter)|
			Q(job__job_number__icontains=custom_filter)|
			Q(supervisor__icontains=custom_filter)|
			Q(mjs__mjs_number__icontains=custom_filter)).order_by('date')
		
		
    if days_off_only:
        obj = obj.filter(
			Q(user = request.user)&
			Q(date__gte=start_date)&
			Q(date__lte=end_date)&
			Q(description__in=DAYS_OFF)).order_by('date')
		

	######
	# mjs_counted_hours = hours_by_mjs(request, obj)
	

    total = calc_time(obj)

    horas = total_time(total)	
    html_string = render_to_string(template_name,{'obj':obj, 'user':user, 'total':horas,'user_profile':user_profile, 'timesheet_number':str(obj.last().id).zfill(6)})
    html = HTML(string = html_string)
    pdf = html.write_pdf(target=f'/tmp/{user.first_name}_{user.last_name}_timesheet.pdf', stylesheets=[])

    fs = FileSystemStorage('/tmp')
    with fs.open(f'{user.first_name}_{user.last_name}_timesheet.pdf') as pdf:
        html_content = render_to_string('send_timesheet_email.html',{'first_name':request.user.first_name, 'last_name':request.user.last_name,'email':request.user.email})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(f'{request.user.first_name} {request.user.last_name} timesheet({start_date[5:]}__{end_date[5:]})', text_content, 'novagenesisnz@gmail.com',[email,request.user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.attach_file(f'/tmp/{user.first_name}_{user.last_name}_timesheet.pdf')
        msg.send()
        return JsonResponse({}, status=200)


def dayoff_add_pwa(request):
    if request.method == 'POST':
        data = json.loads(request.body).get('data')
        mjs = MjsNumber.objects.filter(user = request.user)[0]
        job = mjs.mjs_job
        if mjs.user != request.user:
            raise Http404
        job = get_object_or_404(JobNumber, pk=mjs.mjs_job.id)
        if job.user != request.user:
            raise Http404
        description = data.get('description')
        if not description:
            return JsonResponse({'status':'error', 'message':'Leave type is required'})
        start_date = datetime.datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(data['end_date'], '%Y-%m-%d').date()
        dayoff_data = {
            'user': request.user,
            'client': description,
            'address': description,
            'mjs': mjs,
            'job': job,
            'description': description,
            'time_in': '00:00',
            'time_out': '00:00',
            'break_time': False,
            'supervisor': '----',
            
        }
        rows = 1
        if start_date < end_date:
            rows = 0
            
            while start_date <= end_date:
                dayoff_data['date'] = start_date
                Timesheet.objects.create(**dayoff_data)
                start_date = start_date + datetime.timedelta(days=1)
                rows += 1
            
        else:
            dayoff_data['date'] = start_date
            Timesheet.objects.create(**dayoff_data)
        return JsonResponse({'status':'success', 'message':f'{rows} {description} rows was added to your timesheet' if rows > 1 else f'{rows} {description} row was added to your timesheet'})
        
    return JsonResponse({'status':'ok'})




@login_required(redirect_field_name='accounts:login')
def add_timesheet_json(request):
    if request.method == 'POST':
        data  = json.loads(request.body)
        mjs_number = get_object_or_404(MjsNumber, pk=data['mjs'])
        if mjs_number.user != request.user:
            raise Http404
        job_number = get_object_or_404(JobNumber, pk = mjs_number.mjs_job.id)
        if job_number.user != request.user:
            raise Http404
        client = job_number.job_client.client_name
        supervisor = job_number.job_supervisor.supervisor_name
        address = job_number.job_address
        description = data.get('mjs_description', mjs_number.mjs_description)
        time_in = data.get('time_in')
        time_out = data.get('time_out')
        start_date = datetime.datetime.strptime(data['start'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(data['end'], '%Y-%m-%d').date()
        break_time = data["break_time"]
        ts_data = {
            'user': request.user,
            'mjs': mjs_number,
            'job': job_number,
            'client': client,
            'address': address,
            'description': description,
            'time_in': time_in,
            'time_out': time_out,
            'break_time': break_time,
            'supervisor': supervisor,
        }
        # ts = Timesheet.objects.create(**ts_data)
        # ts.save()
        rows = 1
        if start_date < end_date:
            rows = 0
            while start_date <= end_date:
                
                ts_data['date'] = start_date
                timesheet_validator(request, ts_data)
                start_date = start_date + datetime.timedelta(days=1)
                rows += 1
        else:
            ts_data['date'] = start_date
            timesheet_validator(request, ts_data)
        return JsonResponse({'status':'success', 'rows':rows})
    return JsonResponse({'status':'ok'})


#TODO criar campo para alterar email e nome
#TODO https://data.linz.govt.nz/services;key=441c0097257f45ab84d5ea4d24723f23/wfs?service=WFS&request=GetFeature&outputformat=json&typeNames=layer-53353
#TODO alterar job report



@login_required(redirect_field_name='accounts:login')
def dayoff_add_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mjs = get_object_or_404(MjsNumber, pk=data['mjs'])
        if mjs.user != request.user:
            raise Http404
        job = get_object_or_404(JobNumber, pk=mjs.mjs_job.id)
        if job.user != request.user:
            raise Http404
        description = data.get('description')
        if not description:
            return JsonResponse({'status':'error', 'message':'Description is required'})
        start_date = datetime.datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(data['end_date'], '%Y-%m-%d').date()
        dayoff_data = {
            'user': request.user,
            'client': description,
            'address': description,
            'mjs': mjs,
            'job': job,
            'description': description,
            'time_in': '00:00',
            'time_out': '00:00',
            'break_time': False,
            'supervisor': '----',
            
        }
        rows = 1
        if start_date < end_date:
            rows = 0
            while start_date <= end_date:
                dayoff_data['date'] = start_date
                Timesheet.objects.create(**dayoff_data)
                start_date = start_date + datetime.timedelta(days=1)
                rows += 1
            
        else:
            dayoff_data['date'] = start_date
            Timesheet.objects.create(**dayoff_data)
        return JsonResponse({'status':'success', 'message':f'{rows} {description} rows was added to your timesheet' if rows > 1 else f'{rows} {description} row was added to your timesheet'})

    return JsonResponse({'status':'ok'})

@login_required(redirect_field_name='accounts:login')
def timesheet_validator(request, data):
    dados = Timesheet(user =request.user,
        date = data['date'],
        client = data['client'],
        address = data['address'],
        job = data['job'],
        mjs = data['mjs'],
        description = data['description'],
        time_in = data['time_in'],
        time_out = data['time_out'],
        break_time = data['break_time'],
        supervisor = data['supervisor'])

    mjs = data.get('mjs')
    job = data.get('job')
    
    if not mjs.mjs_hours:
        hour = sum_mjs_api(dados.time_in, dados.time_out, dados.break_time)
        mjs.mjs_hours = str(convert_seconds(hour.seconds))[:5]
        mjs.mjs_seconds = hour.seconds
        dados.seconds = hour.seconds
        mjs.save()
    else:
        hours = sum_mjs_api(dados.time_in, dados.time_out, dados.break_time)
        seconds = hours.seconds
        dados.seconds = seconds
        
        seconds_from_mjs = mjs.mjs_seconds
        seconds += seconds_from_mjs
        mjs.mjs_seconds = seconds
        
        mjs.mjs_hours = (str(total_time(datetime.timedelta(seconds=seconds))))
        mjs.save()
    
    if not job.job_hours:
        hour = sum_mjs_api(dados.time_in, dados.time_out, dados.break_time)
        job.job_hours = convert_seconds(hour.seconds)
        job.job_seconds = hour.seconds
        job.save()
    else:
        hours = sum_mjs_api(dados.time_in, dados.time_out, dados.break_time)
        seconds = hours.seconds
        
        seconds_from_mjs = job.job_seconds
        seconds += seconds_from_mjs
        job.job_seconds = seconds
        
        job.job_hours = (str(total_time(datetime.timedelta(seconds=seconds))))
        job.save()
    
        dados.save()
        return JsonResponse({'status':'success'})


			
    

@login_required(redirect_field_name='accounts:login')
def daywork_delete(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        for item in data.get('dayworks'):
            ts = Timesheet.objects.get(pk = item)
            mjs_ts = ts.mjs.id
            job_ts = ts.job.id
            job = JobNumber.objects.get(pk = job_ts)
            mjs = MjsNumber.objects.get(pk = mjs_ts)
            if ts.user != request.user or not request.user:
                raise Http404
            # form = TimesheetForm(request.POST, instance = ts)
            if not ts.seconds:
                ts.delete()
            else:
                mjs.mjs_seconds -= ts.seconds
                mjs.mjs_hours = (str(total_time(datetime.timedelta(seconds=mjs.mjs_seconds))))
                mjs.save()
                job.job_seconds -= ts.seconds
                job.job_hours = (str(total_time(datetime.timedelta(seconds=job.job_seconds))))
                job.save()
                ts.delete()
        return JsonResponse({"status":"ok"}, status = 201)
    return JsonResponse({"status":"error"}, status = 400)

    