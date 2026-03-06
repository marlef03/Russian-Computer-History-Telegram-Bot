'''
Script to preload images used in messages
'''


import asyncio
import sys
import logging
import json
from aiogram import Bot
from aiogram.types import FSInputFile
from aiogram.exceptions import TelegramRetryAfter
import src.config as cfg

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


async def main():
    bot = Bot(token=cfg.TOKEN)

    logger.info('Photo preload is started')

    for chapter in range(len(cfg.GENERAL_TEXTS)):
        for page in range(len(cfg.GENERAL_TEXTS[chapter]['contents'])):

            while True:
                try:
                    info = await bot.send_photo(
                        cfg.PRELOAD_CHAT_ID,
                        FSInputFile(cfg.ASSETS_PATH / 'images' / 'general' /
                        cfg.GENERAL_TEXTS[chapter]['contents'][page]['image'])
                    )
                    break
                except TelegramRetryAfter as e:
                    await asyncio.sleep(e.retry_after)

            logger.info(f'Processed general chapter {chapter} page {page}')
            cfg.GENERAL_TEXTS[chapter]['contents'][page]['image_id'] = info.photo[-1].file_id

    for page in range(len(cfg.INVENTIONS_TEXTS)):

        while True:
            try:
                info = await bot.send_photo(
                    cfg.PRELOAD_CHAT_ID,
                    FSInputFile(cfg.ASSETS_PATH / 'images' / 'inventions' /
                    cfg.INVENTIONS_TEXTS[page]['image'])
                )
                break
            except TelegramRetryAfter as e:
                await asyncio.sleep(e.retry_after)

        logger.info(f'Processed inventions page {page}')
        cfg.INVENTIONS_TEXTS[page]['image_id'] = info.photo[-1].file_id

    for page in range(len(cfg.SCIENTISTS_TEXTS)):

        while True:
            try:
                info = await bot.send_photo(
                    cfg.PRELOAD_CHAT_ID,
                    FSInputFile(cfg.ASSETS_PATH / 'images' / 'scientists' /
                    cfg.SCIENTISTS_TEXTS[page]['image'])
                )
                break
            except TelegramRetryAfter as e:
                await asyncio.sleep(e.retry_after)

        logger.info(f'Processed scientists page {page}')
        cfg.SCIENTISTS_TEXTS[page]['image_id'] = info.photo[-1].file_id

    with open(str(cfg.ASSETS_PATH / 'general_texts.json'), 'w', encoding='utf-8') as f:
        json.dump(cfg.GENERAL_TEXTS, f, indent=2, ensure_ascii=False)

    with open(str(cfg.ASSETS_PATH / 'inventions_texts.json'), 'w', encoding='utf-8') as f:
        json.dump(cfg.INVENTIONS_TEXTS, f, indent=2, ensure_ascii=False)

    with open(str(cfg.ASSETS_PATH / 'scientists_texts.json'), 'w', encoding='utf-8') as f:
        json.dump(cfg.SCIENTISTS_TEXTS, f, indent=2, ensure_ascii=False)

    logger.info('Photo preload is done')


if __name__ == '__main__':
    asyncio.run(main())
