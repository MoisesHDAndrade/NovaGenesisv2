from django.core.serializers import serialize
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

import json
from django.utils.crypto import get_random_string
import hashlib
import base64

from backend.apps.client.models import Client
from backend.apps.mjs.models import MjsNumber
from backend.apps.supervisor.models import Supervisor
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import JobNumberSerializer, JobNumberCreatorSerializer
from .models import JobNumber, JobNumberCreator


def encode_base64(link):
    link_bytes = link.encode('utf-8')
    base64_bytes = base64.b64encode(link_bytes)
    base64_link = base64_bytes.decode('utf-8')
    return base64_link

def generate_key():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    simbols = '0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, simbols+chars+chars.upper())
    # autenticado = hashlib.sha256((secret_key).encode('utf-8')).hexdigest()

    return encode_base64(secret_key[:10])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def job_list(request):
   
    job = JobNumber.objects.filter(user = request.user).order_by('-id')
    serializer = JobNumberSerializer(job, many = True)
    return JsonResponse(serializer.data,safe=False ,status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def job_detail(request, pk):
    job = JobNumber.objects.get(pk = pk)
    serializer = JobNumberSerializer(job, many = False)
    return JsonResponse(serializer.data, safe=False)


def validate_client(request, data):
    client = None
    print(data)
    client_data = data.get('clientSelected')
    clients = Client.objects.filter(Q(user = request.user.id))
    results = (cl for cl in clients if cl.client_name.lower() == client_data.lower())
    
    if list(results):
        print('tem')
        
        return None
    else:
        print('nao tem vou criar')
        client = Client.objects.create(user = request.user, client_name = data.get('clientSelected'))
        client.save()
        return client


def validate_supervisor(request, data):
    supervisor = None                                                       #Inicia a varivavel supervisor como none
    supervisor_data = data.get('supervisorSelected')                        #Pega o conteudo do dicionario
    supervisors = Supervisor.objects.filter(Q(user = request.user.id))         #Faz o filtro de todos os supervisores pelo atual user
    results = (sup for sup in supervisors if sup.supervisor_name.lower() == supervisor_data.lower())        #retorna um generator caso exista o mesmo nome dentro do banco de dados
    
    if list(results):       #caso supervisor com o mesmo nome haja retorna vazio
        return None
    else:
        #caso nao haja nenhum supervisor com o mesmo nome cria um com o nome selecionado
        supervisor = Supervisor.objects.create(user = request.user, supervisor_name = data.get('supervisorSelected'))
        supervisor.save()
        return supervisor

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):
    if request.method == 'POST':
        data = request.data
        data = data.get('data')
        print(data)     
        job = JobNumber(
            user = request.user,
            job_number = data.get('job'),
            # job_client = Client.objects.get(pk = data.get('clientSelected').get('id')),
            job_project = data.get('project'),
            job_address = data.get('addressSelected').get('ad'),
            job_hours = 0,
            job_seconds = 0,
        )
        
        if isinstance(data.get('clientSelected'), dict):
            job.job_client = Client.objects.get(pk = data.get('clientSelected').get('id'))
        
        else:
            client = validate_client(request, data)
            if client:
                job.job_client = client
                print('aqui')
            elif not client:
                print('erro 400')
                status = 400
                message = 'Sorry! you already created this client name'
                return JsonResponse({'status':status, 'message':message})
           

        if isinstance(data.get('supervisorSelected'), dict):
            job.job_supervisor = Supervisor.objects.get(pk = data.get('supervisorSelected').get('id'))
        else:
            # VALIDACAO DO NOME DO SUPERVISOR
            # CASO NAO HAJA UM SUPERVISOR COM O NOME ESPECIFICADO
            # SERA CRIADO UM, TAMBEM IMPEDE O USO DE NOMES CASE SENSITIVE
            supervisor = validate_supervisor(request, data)
            print(f'O que chega em  {type(supervisor)}' )
            if supervisor:
                job.job_supervisor = supervisor
                print('aqui')
            elif not supervisor:
                print('erro 400')
                status = 400
                message = 'Sorry! you already created this supervisor name'
                return JsonResponse({'status':status, 'message':message})
            # try:
            #     # Tenta pegar o cliente se ele existir
                
            #     job.job_supervisor = Supervisor.objects.get(pk = data.get('supervisorSelected').get('id'))
            # except:
            #     supervisor = validate_supervisor(request, data)
            #     print(f'O que chega em  {type(supervisor)}' )
            #     if supervisor:
            #         job.job_supervisor = supervisor
            #         print('aqui')
            #     elif not supervisor:
            #         print('erro 400')
            #         status = 400
            #         message = 'Sorry! you already created this supervisor name'
            #         return JsonResponse({'status':status, 'message':message})

        job.save()
        return JsonResponse({'status':'201'}, status="201")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def job_delete(request, pk):
    job = JobNumber.objects.get(pk = pk)
    if not request.user.is_authenticated:
        pass
    if job.user != request.user:
        return JsonResponse({}, status=400)
    if request.method == 'POST':
        job.delete()
        return JsonResponse({'message':f'{job.job_number} was deleted with success'}, status=200)


    
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def job_update(request, pk):
    job = JobNumber.objects.get(pk = pk)
    # TODO Criar funcao para fazer autenticacao de usuario
    status = 200
    message = ''
    if not request.user.is_authenticated:
        pass
    if job.user != request.user:
        return JsonResponse({}, status=400)
    
    if request.method == "POST":
        data = json.loads(request.body).get('data')
        print(data)
        
        if isinstance(data.get('clientSelected'), dict):
            job.job_client = Client.objects.get(pk = data.get('clientSelected').get('id'))
        else:
            client = validate_client(request, data)
            if client:
                job.job_client = client
               
            elif not client:
                job.job_client = job.job_client
                # status = 400
                # message = 'Sorry! you already created this client name'
                # return JsonResponse({'status':status, 'message':message})
           

        if isinstance(data.get('supervisorSelected'), dict):
            job.job_supervisor = Supervisor.objects.get(pk = data.get('supervisorSelected').get('id'))
        else:
            supervisor = validate_supervisor(request, data)
            if supervisor:
                job.job_supervisor = supervisor
                
            elif not supervisor:
                job.job_supervisor = job.job_supervisor
                # status = 400
                # message = 'Sorry! you already created this supervisor name'
                # return JsonResponse({'status':status, 'message':message})

        if isinstance(data.get('addressSelected'), dict):
            job.job_address = data.get('addressSelected').get('ad')

        if not data.get('addressSelected'):
            job.job_address = job.job_address
        
        job.user = request.user
        job.job_number = data.get('job') if data.get('job') else job.job_number
        job.job_project = data.get('project') if data.get('project') else job.job_project
        job.job_hours = job.job_hours
        job.job_seconds = job.job_seconds
     
        
        job.save()
        return JsonResponse({'status':status, 'message':message})


def job_sharer_creator(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        creator = JobNumberCreator.objects.filter(user =request.user)
        if not creator:
            creator.create(
                user = request.user,
                
                **data
            )
            creator.chave = generate_key(),
            creator.save()
        else:
            creator[0].user = request.user
            creator[0].chave = generate_key()
            creator[0].job_number = data.get('job_number')
            creator[0].job_client = data.get('job_client')
            creator[0].job_project = data.get('job_project')
            creator[0].job_address = data.get('job_address')
            creator[0].job_supervisor = data.get('job_supervisor')
            creator[0].mjs_number = data.get('mjs_number')
            creator[0].mjs_description = data.get('mjs_description')
            creator[0].save()

            serializer = JobNumberCreatorSerializer(creator[0], many = False)
        return JsonResponse(serializer.data, safe = False)
    return JsonResponse({})


def get_key_job_sharer_creator(request, key):
    
    jbc = JobNumberCreator.objects.get(chave = key)
    # job = JobNumber.objects.get_or_create(job_number = jbc.job_number, user=request.user)
    jobs = JobNumber.objects.filter(user = request.user)
   
    job_results = (job for job in jobs if job.job_number == jbc.job_number)
    print(list(job_results))
    
    if job_results:
        # job = jobs.get_or_create(job_number = jbc.job_number)
        mjss = MjsNumber.objects.filter(Q(user = request.user) )
        print(mjss)
        mjs_results = (mjs for mjs in mjss if mjs.mjs_number == jbc.mjs_number)

    serializer = JobNumberCreatorSerializer(jbc, many = False)
    # if not job[1]:
    #     return JsonResponse({'status':400,'message':f'Do you want create job {jbc.job_number}?', 'data':serializer.data})
    # else:
    #     print('ja tem')
    
    return JsonResponse({})