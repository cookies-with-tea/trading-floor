import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_get_me(user_data: dict):
    api = APIClient(enforce_csrf_checks=True)

    user = User(**user_data)
    user.save()

    api.force_authenticate(user)

    response = api.get(reverse('user-me'))
    response_content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_content['id'] == user.id
    assert response_content['first_name'] == user.first_name
    assert response_content['email'] == user.email
