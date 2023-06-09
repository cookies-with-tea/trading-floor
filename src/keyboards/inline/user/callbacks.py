from aiogram.filters.callback_data import CallbackData


class ProfileCallbackFactory(CallbackData, prefix='profile'):
    action: str
