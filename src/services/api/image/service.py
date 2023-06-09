from src.models.media import Image
from src.services.api.base import API
from src.services.base import SingletonService


class ImageAPIService(SingletonService, API):
    @staticmethod
    def to_model(data: dict) -> Image:
        return Image(
            id=data['id'],
            url=data['url'],
        )

    @classmethod
    def to_models(cls, data: dict) -> list[Image]:
        return [cls.to_model(item) for item in data]
