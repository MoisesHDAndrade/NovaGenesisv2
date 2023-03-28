
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from backend.apps.job.models import JobNumber
from backend.apps.job.serializers import JobNumberSerializer
from backend.apps.mjs.models import MjsNumber


from . serializers import UserProfileSerializer
from . models import UserProfile
import json
import datetime




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail_json_pwa(request):
    """
    Retorna os ultimos 6 jobs com as maiores quantidades de horas
    """
    job = JobNumber.objects.filter(user = request.user)
    job_seconds = job.order_by('-job_seconds').filter(Q(job_seconds__isnull = False)).order_by('-job_seconds')
    if job_seconds:
        if len(job_seconds) > 6:
            job_seconds = job_seconds[:6]
            serializer = JobNumberSerializer(job_seconds, many = True)
            return JsonResponse(serializer.data, safe = False)
    serializer = JobNumberSerializer(job_seconds, many = True)
    return JsonResponse(serializer.data, safe = False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    user_info = {
        'first_name':request.user.first_name,
        'last_name':request.user.last_name,
        'email':request.user.email,
        'position':request.user.user_profile.user_position,
        'phone':request.user.user_profile.user_phone_number,
        }
    return JsonResponse(user_info, safe=False)
    









##################################################################################3

def login(request):
    pass

def get_authentication(request):
    if request.user.is_authenticated:
        return JsonResponse({'status':'200','authenticated':True})
    else:
        return JsonResponse({'status':'200','authenticated':False})

@login_required
def user_detail_json(request):
    job = JobNumber.objects.filter(user = request.user)
    job_seconds = job.order_by('-job_seconds').filter(Q(job_seconds__isnull = False)).order_by('-job_seconds')
    if job_seconds:
        if len(job_seconds) > 6:
            job_seconds = job_seconds[:6]
            serializer = serializers.serialize('json', job_seconds)
            return JsonResponse(serializer, safe=False)
    serializer = serializers.serialize('json', job_seconds)
    return JsonResponse(serializer, safe=False)
    
@login_required
def user_detail_json_mjs(request):
    mjs = MjsNumber.objects.filter(user = request.user)
    mjs_seconds = mjs.order_by('-mjs_seconds').filter(Q(mjs_seconds__isnull = False)).order_by('-mjs_seconds')
    if mjs_seconds:
        if len(mjs_seconds) > 6:
            mjs_seconds = mjs_seconds[:6]
            serializer = serializers.serialize('json', mjs_seconds)
            return JsonResponse(serializer, safe=False)
    serializer = serializers.serialize('json', mjs_seconds)
    return JsonResponse(serializer, safe=False)

def user_job_hours(request):
    job = JobNumber.objects.filter(user = request.user)
    serializer = serializers.serialize('json', job)
    return JsonResponse(serializer, safe=False)

def user_profile_update(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user = request.user)
        data = json.loads(request.body)
        user_profile.user_company = data.get("company") if data.get("company") else user_profile.user_company
        user_profile.user_position = data.get("position") if data.get("position") else user_profile.user_position
        user_profile.user_gender = data.get("avatar") if data.get("avatar") else user_profile.user_gender
        user_profile.user_email_destiny = data.get("email") if data.get("email") else user_profile.user_email_destiny
        user_profile.user_phone_number = data.get("phone") if data.get("phone") else user_profile.user_phone_number 
        user_profile.user_car_registration = data.get("car_registration") if data.get("car_registration") else user_profile.user_car_registration
        user_profile.user_car_make = data.get("car_make") if data.get("car_make") else user_profile.user_car_make
        user_profile.user_car_model = data.get("car_model") if data.get("car_model") else user_profile.user_car_model
        user_profile.user_car_wof = data.get("wof") if data.get("wof") else user_profile.user_car_wof
        user_profile.user_car_rego = data.get("rego") if data.get("rego") else user_profile.user_car_rego
        user_profile.user_date_next_service = data.get("date_next_service") if data.get("date_next_service") else user_profile.user_date_next_service
        user_profile.user_next_service_mileage = data.get("next_service_mileage") if data.get("next_service_mileage") else user_profile.user_next_service_mileage
        user_profile.user_kms_paid_up_to = data.get("kms_paid_up_to") if data.get("kms_paid_up_to") else user_profile.user_kms_paid_up_to
        user_profile.save()
    return JsonResponse({"status":"success"},status = 201)