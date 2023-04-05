import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_get_me(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user: User = user_factory(is_active=True)

    api.force_authenticate(user)

    response = api.get(reverse('v1:user-me'))
    response_content = response.json()

    assert response.status_code == status.HTTP_200_OK, 'Ожидался 200 статус-код ответа'
    assert response_content['id'] == user.id, 'ID из тела ответа не равен ID пользователя, который был запрошен'
    assert (
        response_content['first_name'] == user.first_name
    ), 'Имя из тела ответа не равен имени пользователя, который был запрошен'
    assert response_content['email'] == user.email, 'В теле ответа нет поля "email", хотя он ожидался'


def test_get_me_without_jwt() -> None:
    api = APIClient(enforce_csrf_checks=True)

    response = api.get(reverse('v1:user-me'))
    response_content = response.json()

    assert response.status_code == status.HTTP_401_UNAUTHORIZED, 'Ожидалось 401 статус-код ответа'
    assert (
        response_content['detail'] == 'Учетные данные не были предоставлены.'
    ), 'Сообщение в поле "detail" не соответствует ожидаемому'


def test_update_me(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user: User = user_factory()

    api.force_authenticate(user)

    change_data = {
        'first_name': 'ChangeFirstName',
        'last_name': 'ChangeLastName',
    }

    response = api.patch(reverse('v1:user-me'), change_data)
    response_content = response.json()

    user.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK, 'Ожидался 200 статус-код ответа'
    assert (
        response_content['first_name'] == user.first_name
    ), 'Имя из тела ответа не равен имени пользователя, который был запрошен'


def test_invalid_update_me(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user: User = user_factory()

    api.force_authenticate(user)

    old_email = user.email

    update_data = {
        'email': 'test@gmail.com',
    }
    response = api.patch(reverse('v1:user-me'), update_data)

    user.refresh_from_db()

    assert response.status_code == status.HTTP_400_BAD_REQUEST, 'Ожидался 400 статус-код ответа'
    assert (
        user.email == old_email
    ), 'У пользователя изменилось поле "email", хотя ожидалось, что это поле не будет изменено'


def test_delete_me(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user: User = user_factory(is_active=True)

    api.force_authenticate(user)

    assert user.is_active

    response = api.delete(reverse('v1:user-me'))

    user.refresh_from_db()

    assert response.status_code == status.HTTP_204_NO_CONTENT, 'Ожидался 204 статус-код ответа'
    assert not user.is_active, 'Ожидалось, что у пользователя поле "is_active" будет равно False'
