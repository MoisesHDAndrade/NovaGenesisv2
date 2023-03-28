from rest_framework import serializers
from .models import Supervisor

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ('id', 'user','supervisor_name')