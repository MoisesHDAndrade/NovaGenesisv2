from django.urls import path
from . import api_views

app_name = 'job_api'

urlpatterns= [
    path('joblist/', api_views.job_list),
    path('create-job/', api_views.create_job),
    path('job-detail/<int:pk>/', api_views.job_detail),
    path('job-delete/<int:pk>/', api_views.job_delete),
    path('job-update/<int:pk>/', api_views.job_update),
    path('job-creator/', api_views.job_sharer_creator),
    path('job-creator-detail/<key>/', api_views.get_key_job_sharer_creator),
]