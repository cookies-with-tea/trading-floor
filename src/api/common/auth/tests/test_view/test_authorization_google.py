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
        picture='https://via.placeholder.com/150/f66b97',
    )


def mock_invalid_google_user():
    return GoogleUser(
        email='testuser@gmail.com',
        picture='https://via.placeholder.com/150/f66b97',
    )


@patch('library.oauth.google.GoogleOauth.create_flow', return_value=None, autospec=True)
@patch('library.oauth.google.GoogleOauth.google_authentication', return_value=mock_google_user(), autospec=True)
def test_authorization_google(
    mock_create_flow,
    mock_google_authentication,
    api_client: APIClient,
) -> None:
    data = {'authorization_code': '1234'}
    response = api_client.post(reverse('common:authorization-google'), data)
    response_content = response.json()

    assert response.status_code == status.HTTP_201_CREATED, 'Ожидался 201 статус-код ответа'
    assert response_content['access'] is not None, 'Ожидалось, что поле "access" будет равно None'
    assert response_content['refresh'] is not None, 'Ожидалось, что поле "refresh" будет равно None'
    assert not response_content['is_register'], 'Ожидалось, что поле "is_register" будет равно False'


@patch('library.oauth.google.GoogleOauth.create_flow', return_value=None, autospec=True)
@patch('library.oauth.google.GoogleOauth.google_authentication', return_value=mock_invalid_google_user(), autospec=True)
def test_invalid_authorization_google(
    mock_create_flow,
    mock_google_authentication,
    api_client: APIClient,
) -> None:
    data = {'authorization_code': '1234'}
    response = api_client.post(reverse('common:authorization-google'), data)
    response_content = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST, 'Ожидался 400 статус-код ответа'
    assert User.objects.count() == 0, 'Ожидалось, что количество пользователей в базе данных будет равно 0'
    assert response_content == {'email': ['Разрешены только адреса домена @mer.ci.nsu.ru']}


def test_sign_up(api_client: APIClient, user_factory) -> None:
    user: User = user_factory(
        email='testuser@mer.ci.nsu.ru',
        avatar=None,
    )

    api_client.force_authenticate(user)

    new_data = {
        'first_name': 'Test123MerCi',
        'last_name': 'Test123MerCiN',
    }

    response = api_client.post(reverse('common:sign-up'), new_data)
    response_content = response.json()

    user.refresh_from_db()

    assert not user.avatar, 'Ожидалось, что в базе данных, поле "avatar" не будет заполнено'
    assert user.avatar_color is not None, 'Ожидалось, что в базе данных, поле "avatar_color" будет не равно null'

    assert response.status_code == status.HTTP_200_OK, 'Ожидался 200 статус-код ответа'
    assert response_content.get('refresh'), 'Ожидалось, что в теле ответа будет поле "refresh"'
    assert response_content.get('access'), 'Ожидалось, что в теле ответа будет поле "access"'
    assert response_content.get('is_register'), 'Ожидалось, что в теле ответа будет поле "is_register" будет равно True'
