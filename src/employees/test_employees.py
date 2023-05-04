import pytest
from rest_framework.test import APIClient

from models import Employee


@pytest.mark.django_db
def test_create_employee():
    client = APIClient()
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "position": "Developer",
        "birth_date": "1990-01-01"
    }
    response = client.post("/employees/", data, format="json")
    assert response.status_code == 201
    assert Employee.objects.count() == 1
    assert Employee.objects.get().first_name == "John"


@pytest.mark.django_db
def test_get_employee_list():
    client = APIClient()
    Employee.objects.create(first_name="John", last_name="Doe", position="Developer", birth_date="1990-01-01")
    response = client.get("/employees/", format="json")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["first_name"] == "John"


@pytest.mark.django_db
def test_get_employee_detail():
    client = APIClient()
    employee = Employee.objects.create(first_name="John", last_name="Doe", position="Developer", birth_date="1990-01-01")
    response = client.get(f"/employees/{employee.id}/", format="json")
    assert response.status_code == 200
    assert response.data["first_name"] == "John"
