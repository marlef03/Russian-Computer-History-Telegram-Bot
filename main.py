import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from src.handlers import router
import src.config as cfg

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

async def main() -> None:
    bot = Bot(
        token=cfg.TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.MARKDOWN_V2
        )
    )
    await bot.set_my_commands(cfg.BOT_COMMAND_LIST)

    dp = Dispatcher()
    dp.include_router(router)

    logger.info('Bot is started')
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Bot is stopped')
