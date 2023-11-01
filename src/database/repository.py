import json
from dataclasses import dataclass
from src.bot.schemas.payment import PaymentSchema
from src.configuration import conf
from src.database.choices import GroupTypeFormat


@dataclass
class PaymentObject:
    coll: conf.db.collection

    async def get_payments(self, payment: PaymentSchema) -> str:
        group_type = GroupTypeFormat[payment.group_type.name].value
        pipeline = [
            {
                '$match': {
                    'dt': {
                        '$gte': payment.dt_from,
                        '$lte': payment.dt_upto
                    }
                }
            }, {
                '$group': {
                    '_id': {
                        '$dateToString': {
                            'format': group_type,
                            'date': '$dt'
                        }
                    },
                    'dataset': {
                        '$sum': '$value'
                    }
                }
            }, {
                '$project': {
                    '_id': 0,
                    'dataset': 1,
                    'labels': '$_id'
                }
            }, {
                '$sort': {
                    'labels': 1
                }
            }, {
                '$group': {
                    '_id': None,
                    'dataset': {
                        '$push': '$dataset'
                    },
                    'labels': {
                        '$push': '$labels'
                    }
                }
            }, {
                '$project': {
                    '_id': 0,
                    'dataset': 1,
                    'labels': 1
                }
            }
        ]

        result = await self.coll.aggregate(pipeline).to_list(length=None)
        return str(json.dumps(result[0]))
