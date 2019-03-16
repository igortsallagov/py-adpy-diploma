from pymongo import MongoClient
from db.db_config import HOST, PORT, RES_DB, RES_COL


def count_documents():
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.estimated_document_count()
        return query


def find_user(user_id):
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.find_one(
            {'id': user_id}
        )
        return query


def find_all():
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.find()
        return query


def get_indexes():
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.get_indexes()
        return query

