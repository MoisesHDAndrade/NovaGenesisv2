from django.urls import path
from . import api_views
app_name = 'timesheet_api'

urlpatterns = [
    path('timesheet-get/<int:page>/', api_views.get_timesheet),
    path('timesheet-add/', api_views.add_timesheet),
    path('timesheet-edit/<int:pk>/', api_views.timesheet_edit),
    path('timesheet-search/', api_views.get_timesheet_search),
    path('timesheet-calendar-range/', api_views.get_timesheet_calendar_range),
    path('timesheet-calendar-modal/', api_views.get_timesheet_calendar_modal),
    path('timesheet-delete/', api_views.timesheet_delete),
    path('timesheet-export/', api_views.timesheet_export),
    path('timesheet-send/', api_views.timesheet_send),
    path('dayoff/', api_views.dayoff_add_pwa),

    path('add/', api_views.add_timesheet_json, name='add_timesheet_json'),
    path('add/dayoff/', api_views.dayoff_add_api, name='dayoff_add_api'),
    path('delete/dayworks/', api_views.daywork_delete, name='delete_dayworks')
]


