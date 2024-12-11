from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse
from pymongo import MongoClient

import logging

logger = logging.getLogger(__name__)

client = MongoClient("mongodb://localhost")
db = client.HW_10


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        logger.info(f"Trying to authenticate: {username} password:{password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if not db.users.find_one({"username": username}):
                db.users.insert_one({
                    "username": username,
                    "password": password,
                    "is_authenticated": True
                })
            return redirect("quotes:index")
        else:
            return redirect("quotes:index")
            # return HttpResponse("Невірний логін чи пароль") 
            
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("quotes:index")


@login_required
def reset_password_view(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password and confirm_password:
            if new_password == confirm_password:
                request.user.password = make_password(new_password)
                request.user.save()
                messages.success(request, "Ваш пароль успішно змінено.")
                return redirect('quotes:index')  # Перенаправити на головну сторінку
            else:
                messages.error(request, "Паролі не співпадають.")
        else:
            messages.error(request, "Будь ласка, заповніть всі поля.")
    
    return render(request, 'users/reset_password.html')