from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from src.bot.services.validate import get_schema
from src.database.repository import PaymentObject

payment_router = Router(name='payment')


@payment_router.message(
    Command(commands='get_payment')
)
async def get_payment(message: Message):
    await message.answer('Отправьте с и по какой период посчитать и единица группировки для этого\nПример: '
                         '{"dt_from":"2022-09-01T00:00:00",'
                         '"dt_upto":"2022-12-31T23:59:00",'
                         '"group_type":"month"}')


@payment_router.message(
    F.text
)
async def get_payment(message: Message, coll_obj: PaymentObject):
    schema_payment = await get_schema(message.text)
    if not schema_payment:
        await message.answer('Проверьте свои данные\nОни должны соответсовать примеру: '
                             '{"dt_from":"2022-09-01T00:00:00",'
                             '"dt_upto":"2022-12-31T23:59:00",'
                             '"group_type":"month | week | day | hour"}')
    result = await coll_obj.get_payments(schema_payment)
    await message.answer(result)
