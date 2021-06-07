from django.test import TestCase
from ..models import Category


class GenerateCategoryTest(TestCase):
    def test_generating(self):
        response = self.client.get('/Test/')
        self.assertEqual(response.status_code, 404)
        Category.objects.create(name='Test', description='Test', image='-')
        response = self.client.get('/Test/')
        self.assertEqual(response.status_code, 200)
        Category.objects.create(name='test', description='Test', image='-')
        response = self.client.get('/Test/')
        self.assertEqual(response.status_code, 200)
