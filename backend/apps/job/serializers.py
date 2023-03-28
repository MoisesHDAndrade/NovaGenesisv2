from rest_framework import serializers
from .models import JobNumber, JobNumberCreator

class JobNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobNumber
        fields = ('id', 'user', 'job_number','job_client','job_project', 'job_address','job_supervisor', 'job_hours', 'job_seconds', 'get_client_name', 'get_supervisor_name')

class JobNumberCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobNumberCreator
        fields = '__all__'