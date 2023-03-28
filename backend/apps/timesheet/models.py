from django.db import models
from django.contrib.auth.models import User
from backend.apps.job.models import JobNumber
from backend.apps.mjs.models import MjsNumber
import datetime
from datetime import timedelta



class Timesheet(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	date = models.DateField()
	client = models.CharField('Client', max_length=100,blank=True, null=True)
	address = models.CharField('Address', max_length=255,blank=True, null=True)
	job = models.ForeignKey(JobNumber, on_delete = models.CASCADE)
	mjs = models.ForeignKey(MjsNumber, on_delete = models.CASCADE)
	description = models.CharField('Description', max_length=200, null = True, blank=True)
	time_in = models.TimeField(blank=True, null=True)
	time_out = models.TimeField(blank=True, null=True)
	break_time = models.BooleanField(default = False)
	supervisor = models.CharField('Supervisor', max_length=100)
	seconds = models.IntegerField(null = True, blank=True)

	lista = []

	def __str__(self):
		return f'{self.job}'

	def get_job_number(self):
		return self.job.job_number
	
	def get_mjs_number(self):
		return self.mjs.mjs_number
	
	def get_project_name(self):
		return self.job.job_project
	
	def horas(self, tempo1, tempo2):
		if tempo1 and tempo2:
			datetimeFormat = '%H:%M:%S'
			diff = datetime.datetime.strptime(
    			str(tempo2), datetimeFormat) - datetime.datetime.strptime(str(tempo1), datetimeFormat)

			return diff

	def getHoras(self):
		return Timesheet.horas(self, self.time_in, self.time_out)

	def breakTime(self, tempo1, tempo2):
		if tempo1 and tempo2:
			datetimeFormat = '%H:%M:%S'
			parada = datetime.timedelta(minutes=30)
			diff = datetime.datetime.strptime(
			str(tempo2), datetimeFormat) - datetime.datetime.strptime(str(tempo1), datetimeFormat)
			breaktime = diff - parada
			return breaktime
		return None

	def getBreak(self):
		return Timesheet.breakTime(self, self.time_in, self.time_out)

	def string_getBreak(self):
		return str(self.getBreak())

	def string_getHoras(self):
		return str(self.getHoras())