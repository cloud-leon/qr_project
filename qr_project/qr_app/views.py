from django.shortcuts import render
import qrcode
import jwt
import base64
from io import BytesIO
from datetime import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import QRCode
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token



JWT_SECRET = settings.SECRET_KEY  # Use Django's secret key for JWT encoding

# Generate QR Code
@api_view(['POST'])
def generate_qr(request):
    qr_id = str(int(datetime.now().timestamp()))  # Generate a unique timestamp-based ID
    qr_data = f"{qr_id}"  # or any other data you want embedded

    # Generate QR code image (optional)
    img = qrcode.make(qr_data)

    buffered = BytesIO()
    img.save(f"qr_images/{qr_id}.png")
    img.save(buffered, format="PNG")

    img_str = base64.b64encode(buffered.getvalue).decode()
    

    
    # Save QR code data in the database
    qr_code = QRCode.objects.create(
        qr_id=qr_id,
        qr_data=qr_data,
        status='pending'
    )

    return JsonResponse({
        'qr_id': qr_code.qr_id,
        'qr_data': qr_code.qr_data,
        'qr_image_base64': img_str,
    })  


@api_view([''])

# Verify QR Code
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_qr(request):
    qr_id = request.data.get('qr_id')
    qr_code = get_object_or_404(QRCode, qr_id=qr_id)

    if qr_code.status == 'verified':
        return JsonResponse({'message': 'QR code already verified'}, status=400)

    qr_code.status = 'verified'
    qr_code.verified_at = datetime.now()
    qr_code.save()

    return JsonResponse({'message': 'QR code verified successfully'})

# Check QR Code Status
@api_view(['GET'])
def check_qr_status(request, qr_id):
    qr_code = get_object_or_404(QRCode, qr_id=qr_id)
    return JsonResponse({'status': qr_code.status})




