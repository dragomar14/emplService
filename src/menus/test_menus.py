import pytest
from rest_framework.test import APIClient

from models import Menu


@pytest.fixture
def menu():
    return Menu.objects.create(name='Test Menu')


@pytest.fixture
def api_client():
    return APIClient()


def test_menu_list(api_client, menu):
    url = '/api/menus/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == menu.name


def test_menu_detail(api_client, menu):
    url = f'/api/menus/{menu.pk}/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == menu.name
