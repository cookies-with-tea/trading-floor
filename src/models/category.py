from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    title: str
    id: Optional[int] = None
