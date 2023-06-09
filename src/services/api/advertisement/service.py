from src.models.advertisement import Advertisement
from src.services.api.base import API
from src.services.api.category.service import CategoryAPIService
from src.services.api.image.service import ImageAPIService
from src.services.api.user.service import UserAPIService
from src.services.base import SingletonService




class AdvertisementAPIService(SingletonService, API):

    ERROR_NOT_FOUND = {'detail': 'Страница не найдена.'}

    async def get_all_advertisement(self) -> list[Advertisement]:
        response = await self.get('/advertisements')
        return self.to_models(response)

    async def get_advertisement_by_id(self, advertisement_id: int) -> Advertisement | None:
        response = await self.get(f'/advertisements/{advertisement_id}')

        if response == self.ERROR_NOT_FOUND:
            return None

        return self.to_model(response)

    @classmethod
    def to_models(cls, data: dict) -> list[Advertisement]:
        return [cls.to_model(item) for item in data]

    @staticmethod
    def to_model(data: dict) -> Advertisement:
        return Advertisement(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            category=CategoryAPIService.to_model(data['category']),
            images=ImageAPIService.to_models(data['images']),
            urgency_type=data['urgency_type'],
            author=UserAPIService.to_model(data['author'])
        )
