from typing import Dict, Type

from rest_framework.request import Request
from rest_framework.serializers import Serializer


class SerializerClassMapMixin:
    serializer_class_map: Dict[str, Type[Serializer]] = {}

    default_serializer_class: Type[Serializer]
    action: str

    def get_serializer_class(self) -> Type[Serializer]:
        return self.serializer_class_map.get(self.action, self.default_serializer_class)


class SerializerClassMapHttpMethodMixin(SerializerClassMapMixin):
    request: Request

    def get_serializer_class(self) -> Type[Serializer]:
        return self.serializer_class_map.get(self.request.method, self.default_serializer_class)
