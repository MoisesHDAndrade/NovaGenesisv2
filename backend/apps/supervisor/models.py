from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Supervisor(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	supervisor_name = models.CharField('Supervisor', max_length=50)
	
	class Meta:
		unique_together = ('user','supervisor_name',)

	def __str__(self):
		return self.supervisor_name