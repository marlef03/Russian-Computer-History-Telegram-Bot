from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import src.config as cfg


menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['menu']['mode']['text'], 
            callback_data=cfg.BUTTON_TEXT['menu']['mode']['cbd']
        )],
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['menu']['test']['text'], 
            callback_data=cfg.BUTTON_TEXT['menu']['test']['cbd']
        )],
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['menu']['stats']['text'], 
            callback_data=cfg.BUTTON_TEXT['menu']['stats']['cbd']
        )],
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['menu']['settings']['text'], 
            callback_data=cfg.BUTTON_TEXT['menu']['settings']['cbd']
        )]
    ]
)

mode_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['mode']['general']['text'], 
            callback_data=cfg.BUTTON_TEXT['mode']['general']['cbd']
        )],
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['mode']['inventions']['text'], 
            callback_data=cfg.BUTTON_TEXT['mode']['inventions']['cbd']
        )],
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['mode']['scientists']['text'], 
            callback_data=cfg.BUTTON_TEXT['mode']['scientists']['cbd']
        )],
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['mode']['back']['text'],
            callback_data=cfg.BUTTON_TEXT['mode']['back']['cbd']
        )]
    ]
)


general_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text=chapter['title'],
            callback_data=f'general_{i}_0'
        )]
        for i, chapter in enumerate(cfg.GENERAL_TEXTS)
    ] + 
    [
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['general']['back']['text'],
            callback_data=cfg.BUTTON_TEXT['general']['back']['cbd']
        )]
    ]
)


def get_general_reading_keyboard(chapter: int, page: int) -> list[list[InlineKeyboardButton]]:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            ([
                InlineKeyboardButton(
                    text=cfg.BUTTON_TEXT['general_reading']['prev']['text'],
                    callback_data=f'general_{chapter}_{page - 1}'
                )
            ] if page > 0 else []) +
            [
                InlineKeyboardButton(
                    text=cfg.BUTTON_TEXT['general_reading']['page']['text']
                      .format(page + 1, len(cfg.GENERAL_TEXTS[chapter]['contents'])),
                    callback_data=cfg.BUTTON_TEXT['general_reading']['page']['cbd']
                )
            ] + 
            ([
                InlineKeyboardButton(
                    text=cfg.BUTTON_TEXT['general_reading']['next']['text'],
                    callback_data=f'general_{chapter}_{page + 1}'
                )
            ] if page + 1 < len(cfg.GENERAL_TEXTS[chapter]['contents']) else []),
            [InlineKeyboardButton(
                text=cfg.BUTTON_TEXT['general_reading']['back']['text'],
                callback_data=cfg.BUTTON_TEXT['general_reading']['back']['cbd']
            )]
        ]
    )


def get_inventions_keyboard(page: int) -> list[list[InlineKeyboardButton]]:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            ([
                InlineKeyboardButton(
                    text=cfg.BUTTON_TEXT['inventions']['prev']['text'],
                    callback_data=f'inventions_{page - 1}'
                )
            ] if page > 0 else []) +
            [
                InlineKeyboardButton(
                    text=cfg.BUTTON_TEXT['inventions']['page']['text']
                      .format(page + 1, len(cfg.INVENTIONS_TEXTS)),
                    callback_data=cfg.BUTTON_TEXT['inventions']['page']['cbd']
                )
            ] + 
            ([
                InlineKeyboardButton(
                    text=cfg.BUTTON_TEXT['inventions']['next']['text'],
                    callback_data=f'inventions_{page + 1}'
                )
            ] if page + 1 < len(cfg.INVENTIONS_TEXTS) else []),
            [InlineKeyboardButton(
                text=cfg.BUTTON_TEXT['inventions']['back']['text'],
                callback_data=cfg.BUTTON_TEXT['inventions']['back']['cbd']
            )]
        ]
    )


test_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['test']['back']['text'],
            callback_data=cfg.BUTTON_TEXT['test']['back']['cbd']
        )]
    ]
)

stats_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['stats']['back']['text'],
            callback_data=cfg.BUTTON_TEXT['stats']['back']['cbd']
        )]
    ]
)

settings_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text=cfg.BUTTON_TEXT['settings']['back']['text'],
            callback_data=cfg.BUTTON_TEXT['settings']['back']['cbd']
        )]
    ]
)
