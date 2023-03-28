from django.db import models
from django.contrib.auth.models import User
from backend.apps.client.models import Client
from backend.apps.supervisor.models import Supervisor

class JobNumber(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	job_number = models.CharField('Job Number', max_length=50)
	job_client = models.ForeignKey(Client, on_delete = models.CASCADE, verbose_name='Client')
	job_project = models.CharField('Project Name (Optional)', max_length = 100, null=True, blank=True)
	job_address = models.CharField('Job Address', max_length=50)
	job_supervisor = models.ForeignKey(Supervisor, on_delete = models.CASCADE, verbose_name='Supervisor')
	job_hours = models.CharField(max_length = 255, null=True, blank = True)
	job_seconds = models.IntegerField(default = 0, null=True, blank = True)
	# job_longitude = models.FloatField(default = 0, null=True, blank = True)
	# job_latitude = models.FloatField(default = 0, null=True, blank = True)
	
	def __str__(self):
		return self.job_number

	
	def get_client_name(self):
		return self.job_client.client_name

	def get_supervisor_name(self):
		return self.job_supervisor.supervisor_name

class JobNumberCreator(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	chave = models.CharField('Chave', max_length=50, null=True, blank=True)
	job_number = models.CharField('Job Number', max_length=50, null=True, blank=True)
	job_client = models.CharField('Client', max_length = 100, null=True, blank=True)
	job_project = models.CharField('Project Name (Optional)', max_length = 100, null=True, blank=True)
	job_address = models.CharField('Job Address', max_length=50, null=True, blank=True)
	job_supervisor = models.CharField('Supervisor', max_length = 100, null=True, blank=True)
	mjs_number = models.CharField('MJS Number', max_length = 100, null=True, blank=True)
	mjs_description = models.CharField('Description', max_length = 255, null=True, blank=True)

	def __str__(self):
		return self.job_number