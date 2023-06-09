from aiogram.fsm.state import State, StatesGroup


class CreateAdvertisement(StatesGroup):
    input_title = State()
    input_description = State()
    input_category = State()
    input_urgency_type = State()
    input_advertisement_type = State()
    input_image = State()


class SelectAdvertisement(StatesGroup):
    select = State()
