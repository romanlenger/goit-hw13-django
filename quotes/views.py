from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient

from .utils import get_mongodb
from .forms import QuoteForm

client = MongoClient("mongodb://localhost")
db = client.HW_10


def index(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page=per_page)
    quotes_on_page = paginator.page(page)
    
    return render(request, 'quotes/index.html', context={'quotes' : quotes_on_page})


@login_required
def add_quote(request):
    if request.method == "POST":
        author_f = request.POST['author']
        quote = request.POST['quote']
        tags = request.POST['tags']

        if db.authors.find_one({'fullname' : author_f}):
            db.quotes.insert_one({
                'author' : author_f,
                'quote' : quote,
                'tags' : tags,
            })
            return redirect('quotes:index') 
        else:
            return
    else:
        form = QuoteForm()

    return render(request, "quotes/add_quote.html", {"form": form})


