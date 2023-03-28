from django.shortcuts import render
from django.http import JsonResponse

def logout(request):
    return JsonResponse({})

def render_email(request):
    return render(request, 'send_timesheet.html')