import io

import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from pytest_factoryboy import register
from rest_framework.test import APIClient

from factories import AdvertisementFactory, ImageFactory, UserFactory

User = get_user_model()


register(UserFactory)
register(AdvertisementFactory)
register(ImageFactory)


@pytest.fixture(scope='function')
def user_data() -> dict:
    return {
        'first_name': 'TestUserTradingF',
        'last_name': 'TestUserTradingL',
        'room_number': 600,
        'email': 'testtradingfloor@mer.ci.nsu.ru',
        'password': 'testpassword1234',
    }


@pytest.fixture(scope='function')
def advertisement_data() -> dict:
    return {
        'title': 'Test One',
        'description': 'Test description one',
        'advertisement_type': 'EXCHANGE',
        'urgency_type': 'URGENT',
    }


@pytest.fixture(scope='function')
def create_user(user_data):
    return User.objects.create_user(**user_data)


@pytest.fixture(scope='function')
def api_client():
    return APIClient(enforce_csrf_checks=True)


@pytest.fixture
def image_file():
    image = Image.new('RGB', (100, 100), color='red')
    file = io.BytesIO()
    image.save(file, 'jpeg')
    file.seek(0)

    return SimpleUploadedFile('test_image.jpg', file.read(), content_type='image/jpeg')
