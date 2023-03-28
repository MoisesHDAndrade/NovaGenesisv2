from rest_framework import serializers
from .models import MjsNumber

class MjsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MjsNumber
        fields = '__all__'