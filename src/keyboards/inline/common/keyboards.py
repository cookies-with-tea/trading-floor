from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.inline.common.callbacks import CategoryCallbackFactory, MenuCallbackFactory, UrgencyCallbackFactory


def create_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text='Список объявлений',
            callback_data=MenuCallbackFactory(action='list_advertisement').pack(),
        ),
    )

    return builder.as_markup()


def create_choice_category() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text='Одежда',
            callback_data=CategoryCallbackFactory(category='одежда').pack(),
        ),
        InlineKeyboardButton(
            text='Посуда',
            callback_data=CategoryCallbackFactory(category='посуда').pack(),
        ),
        InlineKeyboardButton(
            text='Разное',
            callback_data=CategoryCallbackFactory(category='разное').pack(),
        ),
        *create_back_button(),
    )

    return builder.as_markup()


def create_choice_urgency_type() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text='Срочно',
            callback_data=UrgencyCallbackFactory(urgency='срочно').pack(),
        ),
        InlineKeyboardButton(
            text='Не очень срочно',
            callback_data=UrgencyCallbackFactory(urgency='не очень срочно').pack(),
        ),
        InlineKeyboardButton(
            text='Не срочно',
            callback_data=UrgencyCallbackFactory(urgency='не срочно').pack(),
        ),
        *create_back_button(),
    )

    return builder.as_markup()


def create_back_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(*create_back_button())

    return builder.as_markup()


def create_back_button() -> list[InlineKeyboardButton]:
    return [
        InlineKeyboardButton(
            text='В меню',
            callback_data=MenuCallbackFactory(action='back').pack(),
        )
    ]
