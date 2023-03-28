from django.contrib import admin
from .models import JobNumber, JobNumberCreator
from backend.apps.mjs.models import MjsNumber

class MjsInline(admin.TabularInline):
	model = MjsNumber
	extra = 0


@admin.register(JobNumber)
class JobNumberAdmin(admin.ModelAdmin):
	inlines = (MjsInline,)
	list_display = ('user','job_client','job_number','job_supervisor')
	search_fields = ('job_number',)


admin.site.register(JobNumberCreator)