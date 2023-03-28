from django.contrib import admin
from .models import Supervisor

@admin.register(Supervisor)
class AdminSupervisor(admin.ModelAdmin):
	list_display = ('user','supervisor_name',)
	search_fields = ('supervisor_name',)