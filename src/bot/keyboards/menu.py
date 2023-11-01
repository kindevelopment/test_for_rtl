from aiogram import Bot
from aiogram.types import BotCommand

from src.bot.lexicon.ru_lexicon import Menu_RU


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in Menu_RU.items()
    ]
    await bot.set_my_commands(main_menu_commands)
