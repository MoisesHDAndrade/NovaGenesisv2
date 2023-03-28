from django.contrib import admin
from .models import MjsNumber

@admin.register(MjsNumber)
class MjsNumberAdmin(admin.ModelAdmin):
	list_display = ('user','mjs_number', 'mjs_job',)
	search_fields = ('mjs_number',)