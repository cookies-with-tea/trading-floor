from src.models.category import Category
from src.services.api.base import API
from src.services.base import SingletonService


class CategoryAPIService(SingletonService, API):
    @staticmethod
    def to_model(data: dict) -> Category:
        return Category(
            id=data['id'],
            title=data['title'],
        )
