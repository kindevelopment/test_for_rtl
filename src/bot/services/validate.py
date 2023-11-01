import json
from src.bot.schemas.payment import PaymentSchema


async def get_schema(text: str) -> PaymentSchema | None:
    try:
        data = json.loads(text)
        schema_payment = PaymentSchema(**data)
        return schema_payment
    except (ValueError, TypeError):
        return

