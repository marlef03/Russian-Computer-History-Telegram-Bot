from dotenv import load_dotenv
from os import getenv
from pathlib import Path
import json
from aiogram.types import BotCommand


load_dotenv()
TOKEN = getenv('TOKEN')

BOT_COMMAND_LIST = [
    BotCommand(
        command='/start', 
        description='Запуск бота'
    ),
    BotCommand(
        command='/menu', 
        description='Меню бота'
    ),
    BotCommand(
        command='/mode', 
        description='Выбор режима изучения'
    ),
    BotCommand(
        command='/test', 
        description='Решение тестов'
    ),
    BotCommand(
        command='/stats', 
        description='Прогресс пользователя'
    ),
    BotCommand(
        command='/settings', 
        description='Настройки бота'
    )
]

ASSETS_PATH = Path(__file__).parent.parent / 'assets'

with open(str(ASSETS_PATH / 'replies.json'), encoding='utf-8') as f:
    REPLIES = json.load(f)

with open(str(ASSETS_PATH / 'button_texts.json'), encoding='utf-8') as f:
    BUTTON_TEXT = json.load(f)

with open(str(ASSETS_PATH / 'general_texts.json'), encoding='utf-8') as f:
    GENERAL_TEXTS = json.load(f)

with open(str(ASSETS_PATH / 'inventions_texts.json'), encoding='utf-8') as f:
    INVENTIONS_TEXTS = json.load(f)
