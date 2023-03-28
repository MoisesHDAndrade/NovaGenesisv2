from django.db import models
from django.contrib.auth.models import User
from backend.apps.job.models import JobNumber

class MjsNumber(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	mjs_job = models.ForeignKey(JobNumber, on_delete = models.CASCADE)
	mjs_number = models.CharField('MJS', max_length=50)
	mjs_description = models.CharField('Description', max_length=255, blank=True,null=True)
	mjs_hours = models.CharField( max_length = 255 ,null = True, blank = True)
	mjs_seconds = models.IntegerField(default = 0, null=True, blank=True)
	
	class Meta:
		unique_together = ('mjs_job', 'mjs_number',)
	def __str__(self):
		return self.mjs_number