import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import load_config
from src.services.api.advertisement.service import AdvertisementAPIService
from src.services.api.user.service import UserAPIService

logger = logging.getLogger(__name__)


def register_all_services(base_url: str):
    AdvertisementAPIService(base_url)
    UserAPIService(base_url)


def register_all_handlers(dp):
    from src.handlers.user.router import user_router

    dp.include_router(user_router)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Starting bot')
    config = load_config('.env')

    storage = MemoryStorage()
    bot = Bot(token=config.tgbot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    register_all_services(config.tgbot.base_url)
    register_all_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
