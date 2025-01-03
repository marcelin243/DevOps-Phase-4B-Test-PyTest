# tests.py
import pytest
from rest_framework.test import APIClient
from myapp.models import Product

@pytest.mark.django_db
class TestProductAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_create_product(self):
        response = self.client.post('/products/', {
            'name': 'New Product',
            'price': 20.00,
            'description': 'A new product'
        })
        assert response.status_code == 201
        assert Product.objects.count() == 1
        assert Product.objects.get().name == 'New Product'

    def test_get_products(self):
        Product.objects.create(name='Test Product', price=19.99, description='Test description')
        response = self.client.get('/products/')
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]['name'] == 'Test Product'

    def test_get_product_detail(self):
        product = Product.objects.create(name='Detail Product', price=15.00, description='Detail description')
        response = self.client.get(f'/products/{product.id}/')
        assert response.status_code == 200
        assert response.data['name'] == 'Detail Product'

    def test_update_product(self):
        product = Product.objects.create(name='Old Product', price=10.00, description='Old description')
        response = self.client.put(f'/products/{product.id}/', {
            'name': 'Updated Product',
            'price': 25.00,
            'description': 'Updated description'
        })
        assert response.status_code == 200
        product.refresh_from_db()
        assert product.name == 'Updated Product'
        assert product.price == 25.00

    def test_delete_product(self):
        product = Product.objects.create(name='Delete Product', price=30.00, description='Delete description')
        response = self.client.delete(f'/products/{product.id}/')
        assert response.status_code == 204
        assert Product.objects.count() == 0

    def test_create_product_invalid(self):
        response = self.client.post('/products/', {
            'name': '',  # Nom vide, ce qui devrait échouer
            'price': 20.00,
            'description': 'A new product'
        })
        assert response.status_code == 400
        assert Product.objects.count() == 0
