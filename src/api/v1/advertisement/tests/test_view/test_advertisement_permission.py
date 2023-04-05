import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.user.models import User

pytestmark = [
    pytest.mark.django_db,
]


def test_get_with_not_rights(api_client: APIClient, user_factory) -> None:
    user: User = user_factory()
    user.is_active = False

    api_client.force_authenticate(user)

    response = api_client.get(reverse('v1:advertisements-list'))

    assert response.status_code == status.HTTP_403_FORBIDDEN
