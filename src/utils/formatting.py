from src.models.advertisement import Advertisement
from src.models.user import User


def format_list_advertisement(advertisements: list[Advertisement]) -> str:
    result = ''

    for item in advertisements:
        result += f'{item.id} | {item.title}\n'

    return result


def format_detail_advertisement(advertisement: Advertisement) -> str:
    return f'{advertisement.id} | {advertisement.title} | {advertisement.category.title}\n\n{advertisement.description}'


def format_profile(user: User) -> str:
    return f'{user.id} | {user.first_name} {user.last_name} | {user.created_at}\n\nПочта: example@gmail.com\n\nКоличество открытых сделок: 3'


def format_respond_profile(user: User) -> str:
    text = ''
    text += f'Имя: {user.first_name}\n'

    if user.last_name:
        text += f'Фамилия: {user.last_name}\n'

    text += f'Номер комнаты: {user.room_number}\n'

    if user.telegram_username:
        text += f'Telegram: {user.telegram_username}\n'

    if user.vk_username:
        text += f'VK: {user.vk_username}\n'

    return text
