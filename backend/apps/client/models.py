from django.db import models
from django.contrib.auth.models import User
class Client(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, )
	client_name = models.CharField('Client', max_length=50)

	class Meta:
		unique_together = ('user','client_name')
		
	def __str__(self):
		return self.client_name
