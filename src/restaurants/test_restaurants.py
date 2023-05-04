import pytest
from rest_framework.test import APIClient

from models import Restaurant


@pytest.fixture
def restaurant():
    return Restaurant.objects.create(name='Test Restaurant')


@pytest.fixture
def api_client():
    return APIClient()


def test_restaurant_list(api_client, restaurant):
    url = '/api/restaurants/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == restaurant.name


def test_restaurant_detail(api_client, restaurant):
    url = f'/api/restaurants/{restaurant.pk}/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == restaurant.name
