from dataclasses import dataclass, field

from aiogram.types import InputMediaPhoto


@dataclass
class Image:
    id: int
    url: str


@dataclass
class InputMediaGroup:
    photos: list[InputMediaPhoto] = field(default_factory=list)

    def to_line_list(self) -> list:
        return self.photos
