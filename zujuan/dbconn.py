#!/usr/bin/env python
#-*-coding:utf-8-*-
from pymongo import MongoClient

def db(tabname='asks'):
    dbhost = 'localhost'
    dbport = 27017
    dbbase = 'zujuan'
    dbcollection = tabname

    client = MongoClient(dbhost, dbport)
    db = client[dbbase]
    collection = db[dbcollection]

    return (client, db, collection)

if __name__ == "__main__":
    db, coll = db()
    import datetime

    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ['a', 'b', 'c'],
        'date': datetime.datetime.utcnow(),
    }

    coll.insert_one(post)

