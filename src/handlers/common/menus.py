from aiogram import types
from src.models.advertisement import Advertisement


def advertisement(
    message: types.Message,
    advertisement: Advertisement,
    is_answer: bool = True,
):
    method_message = message.answer if is_answer else message.edit_text
