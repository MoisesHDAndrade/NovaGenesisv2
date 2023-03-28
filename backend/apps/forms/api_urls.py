from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.get_leave_form),
    path('render-leave-form/', api_views.leave_form_pdf),
    path('products/', api_views.get_products),
]