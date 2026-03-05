'''
Module with definitions of message handlers
'''


import logging
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram import Router
from src.schemas import User
import src.keyboards as kbs
import src.config as cfg

logger = logging.getLogger(__name__)

router = Router()
'''Root handlers router'''

users = {}
'''Dictionary, that stores user info'''


# Handler for start option

@router.message(CommandStart())
async def start_command_handler(message: Message):
    '''
    Function that handles a /start command

    :param message: Message object
    '''

    logger.info(
        f'User {message.from_user.username} with '
        f'id {message.from_user.id} performed a /start command'
    )

    user_id = message.from_user.id
    if user_id not in users:
        logger.info('Unknown user, creating a new record')

        users[user_id] = User(
            user_id,
            None,
            0,
            [],
            []
        )

    await message.answer(cfg.REPLIES['welcome'].format(message.from_user.first_name))

    await message.answer(cfg.REPLIES['menu'], reply_markup=kbs.menu_keyboard)


# Handler for menu command

@router.message(Command('menu'))
async def menu(message: Message):
    '''
    Function that sends menu message (from command /menu)

    :param message: Message object
    '''

    logger.info(
        f'User {message.from_user.username} with '
        f'id {message.from_user.id} performed a /menu command'
    )

    await message.answer(cfg.REPLIES['menu'], reply_markup=kbs.menu_keyboard)


@router.callback_query(F.data == 'menu')
async def menu(callback_query: CallbackQuery):
    '''
    Function that sends menu message (from callback)

    :param callback_query: CallbackQuery object
    '''

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} entered the menu'
    )

    await callback_query.message.edit_text(cfg.REPLIES['menu'], reply_markup=kbs.menu_keyboard)

    await callback_query.answer()


# Handlers for mode option

@router.callback_query(F.data == 'mode')
async def mode(callback_query: CallbackQuery):
    '''
    Function that sends mode message (from callback)

    :param callback_query: CallbackQuery object
    '''

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} is choosing mode'
    )

    await callback_query.message.answer(cfg.REPLIES['mode'], reply_markup=kbs.mode_keyboard)

    await callback_query.message.delete()

    await callback_query.answer()


@router.message(Command('mode'))
async def mode(message: Message):
    '''
    Function that sends mode message (from command /mode)

    :param message: Message object
    '''

    logger.info(
        f'User {message.from_user.username} with '
        f'id {message.from_user.id} performed a /mode command'
    )

    await message.answer(cfg.REPLIES['mode'], reply_markup=kbs.mode_keyboard)


# Handlers for mode choosing option

@router.callback_query(F.data == 'general')
async def process_general(callback_query: CallbackQuery):
    '''
    Function that sends general mode chapter choice message

    :param callback_query: CallbackQuery object
    '''

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} chose a general mode'
    )

    await callback_query.message.answer(cfg.REPLIES['general'], reply_markup=kbs.general_keyboard)

    await callback_query.message.delete()

    await callback_query.answer()


@router.callback_query(F.data.startswith('general'))
async def process_general_read(callback_query: CallbackQuery):
    '''
    Function that sends general mode message

    :param callback_query: CallbackQuery object
    '''

    chapter, page = map(int, callback_query.data.split('_')[1:])

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} is reading a page {page} '
        f'in chapter {chapter} in general mode'
    )

    await callback_query.message.edit_media(
        InputMediaPhoto(
            media=cfg.GENERAL_TEXTS[chapter]['contents'][page]['image_id'],
            caption=cfg.GENERAL_TEXTS[chapter]['contents'][page]['text']
        ),
        reply_markup=kbs.get_general_reading_keyboard(chapter, page)
    )

    await callback_query.answer()


@router.callback_query(F.data.startswith('inventions'))
async def process_inventions(callback_query: CallbackQuery):
    '''
    Function that sends inventions mode message

    :param callback_query: CallbackQuery object
    '''

    page = int(callback_query.data.split('_')[-1])

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} is reading a page {page} '
        f'in inventions mode'
    )

    await callback_query.message.edit_media(
        InputMediaPhoto(
            media=cfg.INVENTIONS_TEXTS[page]['image_id'],
            caption=cfg.INVENTIONS_TEXTS[page]['text']
        ),
        reply_markup=kbs.get_inventions_keyboard(page)
    )

    await callback_query.answer()


@router.callback_query(F.data.startswith('scientists'))
async def process_scientists(callback_query: CallbackQuery):
    '''
    (!) Not finished

    Function that sends scientists mode message

    :param callback_query: CallbackQuery object
    '''

    page = int(callback_query.data.split('_')[-1])

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} is reading a page {page} '
        f'in scientists mode'
    )

    await callback_query.message.edit_text('На стадии разработки')

    await callback_query.answer()


# Handlers for test option

@router.callback_query(F.data == 'test')
async def test(callback_query: CallbackQuery):
    '''
    (!) Not finished
    
    Function that sends test message (from callback)

    :param callback_query: CallbackQuery object
    '''

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} entered the tests'
    )

    await callback_query.message.edit_text(cfg.REPLIES['test'], reply_markup=kbs.test_keyboard)

    await callback_query.answer()


@router.message(Command('test'))
async def test(message: Message):
    '''
    (!) Not finished
    
    Function that sends test message (from command /test)

    :param message: Message object
    '''

    logger.info(
        f'User {message.from_user.username} with '
        f'id {message.from_user.id} performed a /test command'
    )

    await message.answer(cfg.REPLIES['test'], reply_markup=kbs.test_keyboard)


# Handlers for stats option

@router.callback_query(F.data == 'stats')
async def stats(callback_query: CallbackQuery):
    '''
    (!) Not finished
    
    Function that sends stats message (from callback)

    :param callback_query: CallbackQuery object
    '''

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} entered the stats'
    )

    await callback_query.message.edit_text(cfg.REPLIES['stats'], reply_markup=kbs.stats_keyboard)

    await callback_query.answer()


@router.message(Command('stats'))
async def stats(message: Message):
    '''
    (!) Not finished
    
    Function that sends stats message (from command /stats)

    :param message: Message object
    '''

    logger.info(
        f'User {message.from_user.username} with '
        f'id {message.from_user.id} performed a /stats command'
    )

    await message.answer(cfg.REPLIES['stats'], reply_markup=kbs.stats_keyboard)


# Handlers for settings option

@router.callback_query(F.data == 'settings')
async def settings(callback_query: CallbackQuery):
    '''
    (!) Not finished
    
    Function that sends settings message (from callback)

    :param callback_query: CallbackQuery object
    '''

    logger.info(
        f'User {callback_query.from_user.username} with '
        f'id {callback_query.from_user.id} entered the settings'
    )

    await callback_query.message.edit_text(cfg.REPLIES['settings'], reply_markup=kbs.settings_keyboard)

    await callback_query.answer()


@router.message(Command('settings'))
async def settings(message: Message):
    '''
    (!) Not finished
    
    Function that sends settings message (from command /settings)

    :param message: Message object
    '''

    logger.info(
        f'User {message.from_user.username} with '
        f'id {message.from_user.id} performed a /settings command'
    )

    await message.answer(cfg.REPLIES['settings'], reply_markup=kbs.settings_keyboard)

