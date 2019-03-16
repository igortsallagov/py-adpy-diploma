from pymongo import MongoClient
from datetime import datetime
from db.db_config import HOST, PORT, RES_DB, OFF_COL, START, STEP, STOP


def get_offset():
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[OFF_COL]
        query = collection.find_one()
        if query is None:
            offset = START
        else:
            offset = query['value']
        return offset


def update_offset(offset):
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[OFF_COL]
        date = datetime.today()
        if offset < STOP:
            collection.update_one(
                {'value': offset}, {'$inc': {'value': STEP},
                     '$set': {'date': date}}, upsert=True
                     )
        else:
            collection.update_one(
                {'value': offset}, {'$set': {'value': START,
                    'date': date}}, upsert=True
            )
