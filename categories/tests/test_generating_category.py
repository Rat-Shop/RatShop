from django.test import TestCase
from ..models import ShopCategory


class GenerateCategoryTest(TestCase):
    def test_generating(self):
        response = self.client.get('/sklep/Test/')
        self.assertEqual(response.status_code, 404)
        ShopCategory.objects.create(name='Test', description='Test', image='-')
        response = self.client.get('/sklep/Test/')
        self.assertEqual(response.status_code, 200)
        ShopCategory.objects.create(name='test', description='Test', image='-')
        response = self.client.get('/sklep/Test/')
        self.assertEqual(response.status_code, 200)
