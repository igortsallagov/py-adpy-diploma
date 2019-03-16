from pymongo import MongoClient, DESCENDING
from db.db_config import HOST, PORT, RES_DB, RES_COL


# Returns the number of documents in the collection
def count_documents():
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.estimated_document_count()
        return query


# Returns information about the user with user_id
def find_user(user_id):
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.find_one(
            {'id': user_id}
        )
        return query


# Deletes user with user_id from database
def find_delete_user(user_id):
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.find_one_and_delete(
            {'id': user_id}
        )
        return query


# Returns number of last inserted documents
def get_documents(number):
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.find(
            sort=[('_id', DESCENDING)], limit=number
        )
        return query


# Returns the list of indexes
def get_indexes():
    with MongoClient(HOST, PORT) as client:
        db = client[RES_DB]
        collection = db[RES_COL]
        query = collection.get_indexes()
        return query
