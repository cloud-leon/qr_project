from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import QRCode

class QRCodeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_generate_qr(self):
        response = self.client.post('/api/generate-qr/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('qr_id', response.json())

    def test_verify_qr(self):
        qr_code = QRCode.objects.create(qr_id="12345", qr_data="https://example.com", status="pending")
        response = self.client.post('/api/verify-qr/', {'qr_id': qr_code.qr_id}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        qr_code.refresh_from_db()
        self.assertEqual(qr_code.status, 'verified')
