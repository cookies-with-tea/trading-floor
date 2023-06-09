from aiogram.filters.callback_data import CallbackData


class ProfileCallbackFactory(CallbackData, prefix='profile'):
    action: str


class AdvertisementCallbackFactory(CallbackData, prefix='advertisement'):
    action: str
    advertisement_id: int
