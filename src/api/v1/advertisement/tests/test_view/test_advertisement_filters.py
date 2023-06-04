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

    one_category: AdvertisementCategory = advertisement_category_factory()
    two_category: AdvertisementCategory = advertisement_category_factory()

    for _ in range(10):
        advertisement_factory(category=one_category)

    for _ in range(30):
        advertisement_factory(category=two_category)

    response = api_client.get(reverse('v1:advertisements-list'), data={'category': one_category.id})
    response_json = response.json()

    assert (
            response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, а пришёл {response.status_code}'

    assert (
            len(response_json) == 10
    ), f'Ожидалось, что количество объектов в ответе будет равно 10, но пришло {len(response_json)}'

    response = api_client.get(reverse('v1:advertisements-list'), data={'category': two_category.id})
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

    one_category: AdvertisementCategory = advertisement_category_factory()
    two_category: AdvertisementCategory = advertisement_category_factory()

    for _ in range(10):
        advertisement_factory(category=one_category)

    for _ in range(30):
        advertisement_factory(category=two_category)

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

    one_author: User = user_factory()
    two_author: User = user_factory()
    for _ in range(10):
        advertisement_factory(author=one_author)
    for _ in range(30):
        advertisement_factory(author=two_author)

    api_client.force_authenticate(advertisement.author)

    response = api_client.get(reverse('v1:advertisements-list'), data={'author__id': one_author.id})
    response_json = response.json()
    assert (
            response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert (
        len(response_json) == 10
    ), 'Ожидалось, что все полученные объявления от пользователя номер один'

    response = api_client.get(reverse('v1:advertisements-list'), data={'author__id': two_author.id})
    response_json = response.json()
    assert (
            response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, пришёл - {response.status_code}'
    assert (
        len(response_json) == 30
    ), 'Ожидалось, что все полученные объявления от пользователя номер два'
