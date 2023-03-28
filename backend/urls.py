"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView, TokenVerifyView)
from backend.apps.core.views import logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/logout/', logout, name='token_logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),

    path('api/v1/job/', include('backend.apps.job.api_urls')),


    # path('api/v1/report/',include('backend.apps.report.api_urls')),
    path('api/v1/accounts/', include('backend.apps.account.api_urls')),
    # path('api/v1/clients/', include('backend.apps.client.urls_api')),
    path('core/', include('backend.apps.core.urls')),
    path('api/v1/clients/', include('backend.apps.client.api_urls')),
    path('api/v1/mjs/', include('backend.apps.mjs.api_urls')),
    # # path('api/v1/supervisors/', include('backend.apps.supervisor.urls_api')),
    path('api/v1/supervisors/', include('backend.apps.supervisor.api_urls')),
    path('api/v1/timesheet/', include('backend.apps.timesheet.api_urls')),
    # path('api/v1/leaveform/', include('backend.apps.leaveform.api_urls')),


    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset-password/done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset-password/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
