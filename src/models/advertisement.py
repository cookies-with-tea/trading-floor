from dataclasses import dataclass
from typing import Optional

from src.models.category import Category
from src.models.media import Image


@dataclass
class Advertisement:
    title: str
    description: str
    category: Category
    urgency_type: str
    images: list[Image]
    # author: User
    id: Optional[int] = None
