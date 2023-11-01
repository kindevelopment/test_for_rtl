from aiogram import Dispatcher
from .logic import routers


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    for router in routers:
        dp.include_router(router)

    return dp
