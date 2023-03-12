import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_user_registration(user_data: dict):
    api = APIClient(enforce_csrf_checks=True)

    assert User.objects.count() == 0

    url = reverse('sign-up')
    response = api.post(url, user_data, format='json')
    response_content = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1

    user = User.objects.get(id=response_content['id'])
    assert user.first_name == user_data['first_name']
    assert user.password is not None
    assert user.is_active is True


def test_invalid_user_registration(user_data: dict):
    invalid_user_data = user_data
    invalid_user_data['email'] = 'testemail@gmail.com'

    api = APIClient(enforce_csrf_checks=True)
    url = reverse('sign-up')

    response = api.post(url, invalid_user_data, format='json')
    response_content = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert User.objects.count() == 0
    assert response_content.get('email') is not None
