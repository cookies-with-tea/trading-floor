import pytest
from django.urls import reverse
from rest_framework import status

from apps.advertisement.models import AdvertisementCategory
from apps.user.models import User

pytestmark = [
    pytest.mark.django_db,
]


def test_get_list_categories(api_client, user_factory, advertisement_category_factory) -> None:
    user: User = user_factory()
    api_client.force_authenticate(user)

    for index in range(10):
        advertisement_category_factory(title=f'Category {index}')

    assert (
        AdvertisementCategory.objects.count() == 9
    ), f'Ожидалось, что количество категорий в базе данных будет равно 9, а не {AdvertisementCategory.objects.count()}'

    response = api_client.get(reverse('v1:categories-list'))
    response_json = response.json()

    assert (
        response.status_code == status.HTTP_200_OK
    ), f'Ожидался 200 статус-код ответа, а пришёл {response.status_code}'

    assert (
        len(response_json) == 9
    ), f'Ожидалось, что количество категорий в ответе будет равно 9, а не {len(response_json)}'
