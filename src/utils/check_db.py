from src.configuration import conf


async def check_init_collection(coll: conf.db.collection) -> list:
    a = coll.find()
    return await a.to_list(length=100)
