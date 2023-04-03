import factory.django
from factory.fuzzy import FuzzyInteger

from apps.advertisement.models import Advertisement, Image
from apps.user.models import User


class ImageFactory(factory.django.DjangoModelFactory):
    image = factory.Faker('image_url')

    class Meta:
        model = Image


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    room_number = FuzzyInteger(700, 999)
    avatar = factory.Faker('image_url')

    class Meta:
        model = User


class AdvertisementFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('text')
    description = factory.Faker('paragraph')
    type = factory.Faker('random_element', elements=[item[0] for item in Advertisement.TYPE_LIST])
    image = factory.SubFactory(ImageFactory)
    urgency = factory.Faker('random_element', elements=[item[0] for item in Advertisement.URGENCY_LIST])
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Advertisement
