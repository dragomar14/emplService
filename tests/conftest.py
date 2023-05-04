import pytest
from django.test import Client
from mixer.backend.django import mixer


@pytest.fixture(scope="function")
def client():
    """Django test client"""
    return Client()


@pytest.fixture(scope="function")
def employee_factory():
    """Factory for creating Employee instances"""
    return mixer.blend


@pytest.fixture(scope="function")
def menu_factory():
    """Factory for creating Menu instances"""
    return mixer.blend


@pytest.fixture(scope="function")
def restaurant_factory():
    """Factory for creating Restaurant instances"""
    return mixer.blend
