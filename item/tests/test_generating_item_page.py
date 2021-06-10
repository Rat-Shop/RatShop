from django.test import TestCase
from categories.models import ShopCategory
from ..models import Item


class GenerateCategoryTest(TestCase):
    def test_generating(self):
        response = self.client.get('/przedmiot/1/')
        self.assertEqual(response.status_code, 404)
        ShopCategory.objects.create(name='Test', description='Test', image='')
        response = self.client.get('/Test/')
        self.assertEqual(response.status_code, 200)
        shop = ShopCategory.objects.filter(name='Test').first()
        Item.objects.create(name='Test', description='Test', shop=shop, )
        response = self.client.get('/przedmiot/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/przedmiot/2/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/przedmiot/test/')
        self.assertEqual(response.status_code, 404)



