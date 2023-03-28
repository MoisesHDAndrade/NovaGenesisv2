
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import MjsNumber
from .serializers import MjsSerializer

from backend.apps.job.models import JobNumber
from backend.apps.core.qs_sum_time import total_time

import datetime
import json

class MJSAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        mjs = get_object_or_404(MjsNumber, pk=kwargs['pk'])
        serializer = MjsSerializer(mjs, many=False)
        return Response(serializer.data)


def mjs_copy(request, pk):
    mjs = MjsNumber.objects.get(pk = pk)
    job = str(mjs.mjs_job)
    client = str(mjs.mjs_job.job_client)
    address = str(mjs.mjs_job.job_address)

    return JsonResponse({"mjs":str(mjs), "job":job, "client":client, "address":address})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_mjs(request, pk):
    mjs = MjsNumber.objects.filter(mjs_job = pk).order_by('-id')
    serializer = MjsSerializer(mjs, many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mjs_create(request):
    print('aqi')
    if request.method == "POST":
        data = request.data
        print(data)
        if not data.get('mjs_number'):
            return JsonResponse({'status':'400', 'message':'Ops! Wait a second! MJS Number field can not be empty'})
        
        if not data.get('mjs_description'):
            return JsonResponse({'status':'400', 'message':'Ops! Wait a second! MJS Description field can not be empty'})

        mjs = MjsNumber.objects.create(
            user = request.user,
            mjs_job = JobNumber.objects.get(pk = data.get('job').get('id')),
            mjs_number = data.get('mjs_number'),
            mjs_description = data.get('mjs_description'),
            mjs_hours = 0,
            mjs_seconds = 0
        )
        mjs.save()
        return JsonResponse({'status':201, 'message':f'Yay! Mjs {mjs.mjs_number} was created!'})

    return JsonResponse({}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mjs_delete(request, pk):
    mjs = MjsNumber.objects.get(pk = pk)
    job = JobNumber.objects.get(pk = mjs.mjs_job.id)
    if request.method == "POST":
        if mjs.mjs_hours:
            job.job_seconds -= mjs.mjs_seconds
            job.job_hours = (str(total_time(datetime.timedelta(seconds=job.job_seconds))))
            job.save()
        mjs.delete()
        

        return JsonResponse({'status':200, 'message':f'{mjs.mjs_number} was deleted!'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mjs_update(request, pk):
    mjs = MjsNumber.objects.get(pk =pk)
    if request.method == "POST":
        data = request.data
        print(data)
        if request.user != mjs.user:
            return JsonResponse({'status':400, 'message':'You are not authorized','type':'error'})
        if not data.get('mjs_number'):
            return JsonResponse({'status':400, 'message':'Mjs Number field must be not empty','type':'error'})
        if not data.get('mjs_description'):
            return JsonResponse({'status':400, 'message':'Description field must be not empty','type':'error'})

        if len(data.get('mjs_description')) > 200:
            return JsonResponse({'status':400, 'message':'Description field must be less than 200 characterers','type':'error'})
        mjs.mjs_number = data.get('mjs_number')
        mjs.mjs_description = data.get('mjs_description')
        mjs.save()
        return JsonResponse({'status':200, 'message':f'MJS {mjs.mjs_number} was updated','type':'success'})
    return JsonResponse({}, status = 400)
