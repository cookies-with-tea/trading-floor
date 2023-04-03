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
    response_content = response.json()

    assert response.status_code == status.HTTP_201_CREATED, 'Ожидался 201 статус-код ответа'
    assert Advertisement.objects.count() == 1, 'Ожидалось, что количество объявлений в базе данных будет равно 1'
    assert (
        response_content['title'] == advertisement_data['title']
    ), 'Поле "title" в теле ответа не соответствует изначальным данным'
    assert (
        response_content['description'] == advertisement_data['description']
    ), 'Поле "description" в теле ответа не соответствует изначальным данным'


def test_retrieve_advertisement(api_client: APIClient, advertisement_factory) -> None:
    advertisement: Advertisement = advertisement_factory()

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('advertisements-detail', args=[advertisement.id]))
    response_content = response.json()

    assert response.status_code == status.HTTP_200_OK, 'Ожидался 200 статус-код ответа'
    assert response_content['title'] == advertisement.title
    assert response_content['description'] == advertisement.description


def test_retrieve_invalid_id_advertisement(api_client, advertisement_factory) -> None:
    advertisement: Advertisement = advertisement_factory()

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('advertisements-detail', args=[2]))

    assert response.status_code == status.HTTP_404_NOT_FOUND, 'Ожидался 404 статус-код ответа'


def test_list_advertisement(api_client, advertisement_factory) -> None:
    advertisement: Advertisement = advertisement_factory()
    for _ in range(19):
        advertisement_factory()

    assert Advertisement.objects.count() == 20, 'Ожидалось, что в базе данных будет 20 объявлений'

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('advertisements-list'))
    response_content = response.json()

    assert response.status_code == status.HTTP_200_OK, 'Ожидался 200 статус-код ответа'
    assert (
        len(response_content) == 20
    ), 'Ожидалось, что количество объектов в ответе будет равно количеству объектов в базе данных'
