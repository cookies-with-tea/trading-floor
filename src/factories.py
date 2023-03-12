import factory.django
from factory.fuzzy import FuzzyInteger

from apps.user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    room_number = FuzzyInteger(700, 999)
    avatar = factory.Faker('image_url')

    class Meta:
        model = User
