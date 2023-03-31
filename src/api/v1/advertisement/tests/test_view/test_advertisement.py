import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.advertisement.models import Advertisement
from apps.user.models import User

pytestmark = [
    pytest.mark.django_db,
]


def test_create_advertisement(api_client: APIClient, advertisement_data: dict, user_factory) -> None:
    user: User = user_factory()

    api_client.force_authenticate(user)

    assert Advertisement.objects.count() == 0, 'Ожидалось, что количество объявлений в базе данных будет равно 0'

    response = api_client.post(reverse('advertisements-list'), advertisement_data)

    assert response.status_code == status.HTTP_201_CREATED, 'Ожидался 201 статус-код ответа'
    assert Advertisement.objects.count() == 1, 'Ожидалось, что количество объявлений в базе данных будет равно 1'
