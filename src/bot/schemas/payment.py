from datetime import datetime
from pydantic import BaseModel, model_validator
from src.database.choices import GroupTypeChoices


class PaymentSchema(BaseModel):
    dt_from: str
    dt_upto: str
    group_type: GroupTypeChoices

    @model_validator(mode="after")
    def validate_date(self) -> 'PaymentSchema':
        self.dt_from = datetime.fromisoformat(self.dt_from)
        self.dt_upto = datetime.fromisoformat(self.dt_upto)
        return self
