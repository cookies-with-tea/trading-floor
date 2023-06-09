from aiogram import Router
from aiogram.filters import Command

from src.handlers.user.handlers import router
from src.handlers.user.advertisements.handlers import router as advertisement_router
from src.handlers.user.profile.handlers import router as profile_router

from src.handlers.user.start import start

user_router = Router()
user_router.message.register(start, Command('start'))

user_router.include_router(router)
user_router.include_router(advertisement_router)
user_router.include_router(profile_router)
