# urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('api/send/', views.NotificationAPIView.as_view(), name='send'),

        ]
