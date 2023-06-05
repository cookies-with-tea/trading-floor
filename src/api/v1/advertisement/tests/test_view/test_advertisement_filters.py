import pytest
from django.urls import reverse
from rest_framework import status

from apps.advertisement.models import AdvertisementCategory, Advertisement
from apps.user.models import User

pytestmark = [
    pytest.mark.django_db,
]


def test_filter_advertisement_by_category(
    api_client,
    advertisement_factory,
    advertisement_category_factory,
    user_factory,
) -> None:
    user: User = user_factory()
    api_client.force_authenticate(user)

    first_category: AdvertisementCategory = advertisement_category_factory()
    second_category: AdvertisementCategory = advertisement_category_factory()

    for _ in range(10):
        advertisement_factory(category=first_category)

    for _ in range(30):
        advertisement_factory(category=second_category)

    response = api_client.get(reverse('v1:advertisements-list'), data={'category': first_category.id})
    response_json = response.json()

    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, а пришёл {response.status_code}'

    assert (
        len(response_json) == 10
    ), f'Ожидалось, что количество объектов в ответе будет равно 10, но пришло {len(response_json)}'

    response = api_client.get(reverse('v1:advertisements-list'), data={'category': second_category.id})
    response_json = response.json()

    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, а пришёл {response.status_code}'

    assert (
        len(response_json) == 30
    ), f'Ожидалось, что количество объектов в ответе будет равно 30, но пришло {len(response_json)}'


def test_filter_advertisement_by_invalid_category(
    api_client,
    advertisement_factory,
    advertisement_category_factory,
    user_factory,
) -> None:
    user: User = user_factory()
    api_client.force_authenticate(user)

    first_category: AdvertisementCategory = advertisement_category_factory()
    second_category: AdvertisementCategory = advertisement_category_factory()

    for _ in range(10):
        advertisement_factory(category=first_category)

    for _ in range(30):
        advertisement_factory(category=second_category)

    response = api_client.get(reverse('v1:advertisements-list'), data={'category': 123123})
    response_json = response.json()

    assert (
        response.status_code == status.HTTP_400_BAD_REQUEST
    ), f'Ожидался 400 статус-код ответа, а пришёл {response.status_code}'
    assert 'Выберите корректный вариант. Вашего варианта нет среди допустимых значений.' in response_json['category'], (
        'Ожидалось, что ответ будет содержать поле "category", внутри которого будет находиться строка'
        '"Выберите корректный вариант. Вашего варианта нет среди допустимых значений."'
    )


def test_filter_advertisement_by_author_id(
    api_client,
    advertisement_factory,
    user_factory,
) -> None:
    advertisement: Advertisement = advertisement_factory()

    first_author: User = user_factory()
    second_author: User = user_factory()
    for _ in range(10):
        advertisement_factory(author=first_author)
    for _ in range(30):
        advertisement_factory(author=second_author)

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('v1:advertisements-list'), data={'author__id': first_author.id})
    response_json = response.json()
    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert (
        len(response_json) == 10
    ), 'Ожидалось, что все полученные объявления от пользователя номер один'
    assert (
        _response_json['author']['id'] == first_author.id for _response_json in response_json
    ), 'Ожидалось, что все полученные объявление было создано пользователем номер один'

    response = api_client.get(reverse('v1:advertisements-list'), data={'author__id': second_author.id})
    response_json = response.json()
    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert (
        len(response_json) == 30
    ), 'Ожидалось, что все полученные объявления от пользователя номер два'
    assert (
        _response_json['author']['id'] == second_author.id for _response_json in response_json
    ), 'Ожидалось, что все полученные объявление было создано пользователем номер два'


def test_filter_advertisement_by_is_open(
    api_client,
    advertisement_factory,
) -> None:
    advertisement: Advertisement = advertisement_factory(is_open=True)
    for _ in range(9):
        advertisement_factory(is_open=True)
    for _ in range(20):
        advertisement_factory(is_open=False)

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('v1:advertisements-list'), data={'is_open': True})
    response_json = response.json()
    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert (
        len(response_json) == 10
    ), f'Ожидалось, что все полученных объявлений будет 10, получили {len(response_json)}'
    assert (
        _response_json['is_open'] is True for _response_json in response_json
    ), 'Ожидалось, что все полученные объявления открыты'

    response = api_client.get(reverse('v1:advertisements-list'), data={'is_open': False})
    response_json = response.json()
    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert (
        len(response_json) == 20
    ), f'Ожидалось, что все полученных объявлений будет 20, получили {len(response_json)}'
    assert (
        _response_json['is_open'] is False for _response_json in response_json
    ), 'Ожидалось, что все полученные объявления закрыты'
