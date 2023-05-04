from django.urls import reverse
from rest_framework import status


def test_list_menus(client):
    url = reverse("menu-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_create_menu(client, restaurant_factory):
    url = reverse("menu-list")
    restaurant = restaurant_factory()
    data = {"name": "Test Menu", "description": "Test description", "restaurant": restaurant.id}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


def test_retrieve_menu(client, menu_factory):
    menu = menu_factory()
    url = reverse("menu-detail", args=[menu.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_update_menu(client, menu_factory):
    menu = menu_factory()
    url = reverse("menu-detail", args=[menu.id])
    data = {"name": "Updated Menu", "description": "Updated description"}
    response = client.put(url, data)
    assert response.status_code == status.HTTP_200_OK


def test_delete_menu(client, menu_factory):
    menu = menu_factory()
    url = reverse("menu-detail", args=[menu.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
