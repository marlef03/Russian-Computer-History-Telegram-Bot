'''
Module that stores configuration objects
'''


from dotenv import load_dotenv
from os import getenv
from pathlib import Path
import json
from aiogram.types import BotCommand


load_dotenv()
TOKEN = getenv('TOKEN')
PRELOAD_CHAT_ID = getenv('PRELOAD_CHAT_ID')

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
'''List of supported bot commands'''

ASSETS_PATH = Path(__file__).parent.parent / 'assets'
'''Path object that points to project's assets directory'''

REPLIES: dict = None
'''Dictionary that stores bot replies'''

BUTTON_TEXT: dict = None
'''Dictionary that stores text and callback data of inline buttons'''

GENERAL_TEXTS: list = None
'''Object that stores text and images used in general mode messages'''

INVENTIONS_TEXTS: list = None
'''Object that stores text and images used in inventions mode messages'''

SCIENTISTS_TEXTS: list = None
'''Object that stores text and images used in scientists mode messages'''


with open(str(ASSETS_PATH / 'replies.json'), encoding='utf-8') as f:
    REPLIES = json.load(f)

with open(str(ASSETS_PATH / 'button_texts.json'), encoding='utf-8') as f:
    BUTTON_TEXT = json.load(f)

with open(str(ASSETS_PATH / 'general_texts.json'), encoding='utf-8') as f:
    GENERAL_TEXTS = json.load(f)

with open(str(ASSETS_PATH / 'inventions_texts.json'), encoding='utf-8') as f:
    INVENTIONS_TEXTS = json.load(f)

with open(str(ASSETS_PATH / 'scientists_texts.json'), encoding='utf-8') as f:
    SCIENTISTS_TEXTS = json.load(f)
