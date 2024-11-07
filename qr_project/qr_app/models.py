from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QRCode(models.Model):
    qr_id = models.CharField(max_length=100, unique=True)
    qr_data = models.TextField()
    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.qr_id} - {self.status}"

