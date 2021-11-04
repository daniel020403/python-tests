from django.urls import path
from django.urls.conf import include
from drf_test import views
from rest_framework.routers import DefaultRouter

ApiRouter = DefaultRouter()
ApiRouter.register(r'sms_webhook', views.SmsWebhookViewSet, basename='sms')

urlpatterns = [
    path('', include(ApiRouter.urls)),
]
