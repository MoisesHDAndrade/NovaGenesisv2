from django.contrib import admin
from .models import Timesheet

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
	list_display = ('user','date','job','mjs','time_in', 'time_out')
	search_fields = ('date',)