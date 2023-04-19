import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.advertisement.models import Advertisement, AdvertisementCategory
from apps.user.models import User

pytestmark = [
    pytest.mark.django_db,
]


def test_create_advertisement(
    api_client: APIClient,
    advertisement_data: dict,
    image_file: SimpleUploadedFile,
    user_factory,
    advertisement_category_factory,
) -> None:
    user: User = user_factory()
    category: AdvertisementCategory = advertisement_category_factory()

    api_client.force_authenticate(user)

    data = {
        'title': advertisement_data['title'],
        'description': advertisement_data['description'],
        'advertisement_type': advertisement_data['advertisement_type'],
        'urgency_type': advertisement_data['urgency_type'],
        'images': [image_file],
        'category': category.id,
    }

    assert Advertisement.objects.count() == 0, 'Ожидалось, что количество объявлений в базе данных будет равно 0'

    response = api_client.post(reverse('v1:advertisements-list'), data=data, format='multipart')
    response_content = response.json()

    assert response.status_code == status.HTTP_201_CREATED, 'Ожидался 201 статус-код ответа'
    assert Advertisement.objects.count() == 1, 'Ожидалось, что количество объявлений в базе данных будет равно 1'
    assert (
        response_content['title'] == advertisement_data['title']
    ), 'Поле "title" в теле ответа не соответствует изначальным данным'
    assert (
        response_content['description'] == advertisement_data['description']
    ), 'Поле "description" в теле ответа не соответствует изначальным данным'
    assert len(response_content.get('images', [])) == 1
    assert response_content['images'][0].get('url') is not None


def test_retrieve_advertisement(api_client: APIClient, advertisement_factory) -> None:
    advertisement: Advertisement = advertisement_factory()

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('v1:advertisements-detail', args=[advertisement.id]))
    response_content = response.json()

    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert response_content['title'] == advertisement.title
    assert response_content['description'] == advertisement.description
    assert response_content['category']['title'] == advertisement.category.title


def test_retrieve_invalid_id_advertisement(api_client, advertisement_factory) -> None:
    advertisement: Advertisement = advertisement_factory()

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('v1:advertisements-detail', args=[200]))

    assert (
        response.status_code == status.HTTP_404_NOT_FOUND
    ), f'Ожидался 404 статус-код ответа, пришёл - {response.status_code}'


def test_list_advertisement(api_client, advertisement_factory) -> None:
    advertisement: Advertisement = advertisement_factory()
    for _ in range(19):
        advertisement_factory()

    assert Advertisement.objects.count() == 20, 'Ожидалось, что в базе данных будет 20 объявлений'

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('v1:advertisements-list'))
    response_content = response.json()

    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert (
        len(response_content) == 20
    ), 'Ожидалось, что количество объектов в ответе будет равно количеству объектов в базе данных'
