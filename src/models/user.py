import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    first_name: str
    last_name: str
    room_number: int
    avatar: str
    created_at: datetime.datetime

    telegram_username: Optional[str] = None
    vk_username: Optional[str] = None

    id: Optional[int] = None
