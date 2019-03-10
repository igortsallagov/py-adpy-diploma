from pymongo import MongoClient
from db.db_config import HOST, PORT


def writer(func):
    def insert_to_db(arg):
        with MongoClient(HOST, PORT) as client:
            db = client.vkinder_db
            collection = db.result
            result = func(arg)
            collection.insert_one(result)
            return func(arg)
    return insert_to_db
