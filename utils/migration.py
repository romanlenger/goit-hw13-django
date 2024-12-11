import os
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siteofquotes.settings")
django.setup()

from quotes.models import Quote, Tag, Author
from users.models import User

client = MongoClient("mongodb://localhost")

db = client.HW_10

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname= author['fullname'],
        born_date= author['born_date'],
        born_location = author['born_location'],
        description= author['description']
    )

quotes = db.quotes.find()

for q in quotes:
    tags = []
    for tag in q['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=q['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': q['author']})
        if author is None:
            print(f"Author with id {q['author']} not found in MongoDB.")
        else:
            a = Author.objects.get(fullname=author['fullname'])
            q = Quote.objects.create(
                quote=q['quote'],
                author=a
            )
            for tag in tags:
                q.tags.add(tag)

users = db.users.find()

for user in users:
    User.objects.get_or_create(username=user['username'], password=user['password'])
