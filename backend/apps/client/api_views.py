from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

from rest_framework import generics
from rest_framework import views
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import ClientSerializer
from .models import Client

@method_decorator(login_required, name='dispatch')
class ClientsAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

@method_decorator(login_required, name='dispatch')
class ClientAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
@method_decorator(login_required, name='dispatch')
class ClientByUserAPIView(views.APIView):
    def get(self, request, format = None, *args, **kwargs):
        client = Client.objects.filter(user = kwargs.get('pk')).order_by('client_name')
        serializer = ClientSerializer(client, many = True)
        return response.Response(serializer.data)

# @method_decorator(login_required, name='dispatch')
# class ClientByUserAPIView(views.APIView):
#     def get(self, request, format = None, *args, **kwargs):
#         client = Client.objects.filter(user = kwargs.get('pk')).order_by('client_name')
#         serializer = ClientSerializer(client, many = True)
#         return response.Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_clients(request):
    clients = Client.objects.filter(user_id = request.user.id)
    serializer = ClientSerializer(clients, many = True)
    return JsonResponse(serializer.data, safe = False)
    
def client_create(request):
    print('aqui')
    #  if Client.objects.filter(
    #         Q(client_name=data_from_form.client_name)&
    #         Q(user =data_from_form.user)
    #         ).exists():
    #     return JsonResponse({}, status = True)
                # messages.error(request, 'This client name was already created')
    return JsonResponse({}, status = True)

