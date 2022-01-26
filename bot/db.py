import json

from pymongo import MongoClient

import settings

client = MongoClient(settings.DB)
db = client.chat_db
message_collection = db["message_collection"]


def store_message(msg):
    message_dict = json.loads(str(msg))
    message_collection.insert_one({
        "message": message_dict
    })
