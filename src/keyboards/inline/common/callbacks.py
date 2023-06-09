from aiogram.filters.callback_data import CallbackData


class MenuCallbackFactory(CallbackData, prefix='menu'):
    action: str


class CategoryCallbackFactory(CallbackData, prefix='category'):
    category: str
    
    
class UrgencyCallbackFactory(CallbackData, prefix='urgency'):
    urgency: str
