from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('client_name','user',)
	search_fields = ('client_name',)
	