import bson
from pymongo.results import InsertManyResult

from src.configuration import conf


async def load_json_to_collection(coll: conf.db.collection) -> InsertManyResult:
    with open('../database/dump/sample_collection.bson', 'rb') as f:
        data = bson.decode_all(f.read())
        return coll.insert_many(data)
