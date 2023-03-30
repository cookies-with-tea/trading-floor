from unittest.mock import patch

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from library.oauth.models import GoogleUser

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def mock_google_user():
    return GoogleUser(
        email='testuser@mer.ci.nsu.ru',
    )


@patch('library.oauth.google.GoogleOauth.create_flow', return_value=None, autospec=True)
@patch('library.oauth.google.GoogleOauth.google_authentication', return_value=mock_google_user(), autospec=True)
def test_authorization_google(
    mock_create_flow,
    mock_google_authentication,
    api_client: APIClient,
) -> None:
    data = {'authorization_code': '1234'}
    response = api_client.post(reverse('authorization-google'), data)
    response_content = response.json()

    assert response.status_code == status.HTTP_201_CREATED, 'Ожидался 201 статус-код ответа'
    assert response_content['access'] is not None, 'Ожидалось, что поле "access" будет равно None'
    assert response_content['refresh'] is not None, 'Ожидалось, что поле "refresh" будет равно None'
    assert not response_content['is_active'], 'Ожидалось, что поле "is_active" будет равно False'


def test_sign_up(api_client: APIClient, user_factory) -> None:
    user: User = user_factory(
        email='testuser@mer.ci.nsu.ru',
    )

    api_client.force_authenticate(user)

    new_data = {
        'first_name': 'Test123MerCi',
        'last_name': 'Test123MerCiN',
    }

    response = api_client.post(reverse('sign-up'), new_data)
    response_content = response.json()

    user.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK, 'Ожидался 200 статус-код ответа'
    assert (
        response_content['first_name'] == user.first_name
    ), 'Ожидалось, что поле "first_name" в ответе будет равно полю "first_name" в базе данных'
    assert (
        response_content['last_name'] == user.last_name
    ), 'Ожидалось, что поле "last_name" в ответе будет равно полю "last_name" в базе данных'
