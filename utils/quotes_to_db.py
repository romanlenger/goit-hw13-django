import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient("mongodb://localhost")

db = client.HW_10

with open(r'utils\quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for q in quotes:
    author = db.authors.find_one({'fullname' : q['author']})
    if author:
        db.quotes.insert_one({
            'quote' : q['quote'],
            'tags' : q['tags'],
            'author' : ObjectId(author['_id'])
        })

