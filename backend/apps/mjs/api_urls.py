from django.urls import path
from . import api_views
app_name = 'mjs_api'

urlpatterns = [
    path('detail/<int:pk>/', api_views.MJSAPIView.as_view(), name='detail'),
    path('mjs-copy/<int:pk>/', api_views.mjs_copy),

    # NEW VERSION
    path('get-mjs/<int:pk>/', api_views.get_mjs),
    path('mjs-delete/<int:pk>/', api_views.mjs_delete),
    path('mjs-update/<int:pk>/', api_views.mjs_update),
    path('mjs-create/', api_views.mjs_create),
    # path('update/<int:pk>/', api_views.update_mjs, name = 'update')
]