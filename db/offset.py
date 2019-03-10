from pymongo import MongoClient
from datetime import datetime
from db.db_config import HOST, PORT, START, STEP, STOP


def get_offset():
    with MongoClient(HOST, PORT) as client:
        db = client['vkinder_db']
        collection = db['offset']
        query = collection.find_one()
        if query is None:
            offset = START
        else:
            offset = query['value']
        return offset


def update_offset(offset):
    with MongoClient(HOST, PORT) as client:
        db = client['vkinder_db']
        collection = db['offset']
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
