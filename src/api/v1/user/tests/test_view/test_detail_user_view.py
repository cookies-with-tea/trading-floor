import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_get_detail_user(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = user_factory()

    api.force_authenticate(user)

    response = api.get(reverse('user-detail', kwargs={'pk': user.id}))
    response_content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_content['id'] == user.id
    assert response_content['first_name'] == user.first_name
    assert response_content.get('email') is None


def test_get_detail_unauthorized_user(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = user_factory()

    response = api.get(reverse('user-detail', kwargs={'pk': user.id}))
    response_content = response.json()

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response_content['detail'] == 'Authentication credentials were not provided.'
