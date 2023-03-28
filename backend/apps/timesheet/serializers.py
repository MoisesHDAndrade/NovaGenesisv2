from rest_framework import serializers
from .models import Timesheet

class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = ('id', 
        'user', 
        'date', 
        'client', 
        'address', 
        'job', 
        'mjs', 
        'description', 
        'time_in', 
        'time_out', 
        'break_time', 
        'supervisor', 
        'seconds', 
        'getHoras', 
        'getBreak',
        'get_job_number',
        'get_mjs_number',
        'get_project_name',
        'string_getBreak',
        'string_getHoras')