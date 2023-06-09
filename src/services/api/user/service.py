from datetime import datetime

from src.models.user import User
from src.services.api.base import API
from src.services.base import SingletonService


class UserAPIService(SingletonService, API):
    async def get_user_by_id(self, user_id: int) -> User:
        response = await self.get(f'/users/{user_id}')
        return self.to_model(response)

    @staticmethod
    def to_model(data: dict) -> User:
        return User(
            id=data['id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            room_number=data['room_number'],
            avatar=data['avatar'],
            created_at=datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ'),
        )

    @classmethod
    def to_models(cls, data: dict) -> list[User]:
        return [cls.to_model(item) for item in data]
