from django.urls import path
from . import api_views

urlpatterns = [
    path('all/',api_views.SupervisorsAPIView.as_view()),
    path('create/',api_views.SupervisorCreate.as_view()),

    path('get-supervisors/', api_views.get_supervisors)
]