from django.urls import path
from . import api_views

urlpatterns = [
    path('get-clients/', api_views.get_clients),

    path('all/', api_views.ClientsAPIView.as_view()),
    path('updelete/<int:pk>/', api_views.ClientAPIView.as_view()),
    path('user/<int:pk>/all/', api_views.ClientByUserAPIView.as_view())
]