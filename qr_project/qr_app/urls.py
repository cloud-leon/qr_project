from django.urls import path
from . import views

urlpatterns = [
    path('generate-qr/', views.generate_qr, name='generate_qr'),
    path('verify-qr/', views.verify_qr, name='verify_qr'),
    path('check-qr-status/<str:qr_id>/', views.check_qr_status, name='check_qr_status'),
]

