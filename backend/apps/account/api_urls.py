from django.urls import path
from . import api_views
app_name = 'api_account'

urlpatterns =[
		path('get-authentication/', api_views.get_authentication),
    	path('job/performance/pwa/', api_views.user_detail_json_pwa,),
		path('get-user-info/', api_views.get_user_info),




		########################################################################
		path('user/update', api_views.user_profile_update, name='user_profile_update'),
    	path('job/performance/', api_views.user_detail_json, name = 'detail_json'),
    	path('mjs/performance/', api_views.user_detail_json_mjs, name = 'detail_json_mjs'),
    	path('job/hours/performance/', api_views.user_job_hours, name = 'user_job_hours'),
]