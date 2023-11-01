import asyncio
from aiogram import Bot, Dispatcher

from src.bot.keyboards.menu import set_main_menu
from src.database.repository import PaymentObject
from src.bot.dispatcher import get_dispatcher
from src.configuration import conf
from src.utils.check_db import check_init_collection
from src.utils.json_load import load_json_to_collection


async def start_bot() -> None:
    bot = Bot(token=conf.bot.token)
    dp: Dispatcher = get_dispatcher()
    collection = conf.db.collection
    await set_main_menu(bot)
    coll_obj = PaymentObject(collection)
    if not await check_init_collection(collection):
        await load_json_to_collection(collection)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        coll_obj=coll_obj
    )


if __name__ == '__main__':
    asyncio.run(start_bot())
