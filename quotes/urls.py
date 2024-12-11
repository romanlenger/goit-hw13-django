from django.urls import path, include

from . import views

app_name = "quotes"
 
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:page>', views.index, name="root_paginate"),
    path('users/', include('users.urls')),
    path("add_quote/", views.add_quote, name="add_quote"),
]