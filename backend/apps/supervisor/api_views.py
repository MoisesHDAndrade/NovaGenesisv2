from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from rest_framework import response
from rest_framework import generics
from rest_framework import views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from . serializers import SupervisorSerializer
from . models import Supervisor

@method_decorator(login_required, name = 'dispatch')
class SupervisorsAPIView(views.APIView):
	def get(self, request, format = None, *args, **kwargs):
		
		supervisors = Supervisor.objects.filter(user = self.request.user)
		serializer = SupervisorSerializer(supervisors, many = True)
		return response.Response(serializer.data)
		
@method_decorator(login_required, name = 'dispatch')
class SupervisorCreate(generics.CreateAPIView):
	queryset = Supervisor.objects.all()
	serializer_class = SupervisorSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_supervisors(request):
    supervisors = Supervisor.objects.filter(user = request.user)
    serializer = SupervisorSerializer(supervisors, many = True)
    return JsonResponse(serializer.data, safe=False)