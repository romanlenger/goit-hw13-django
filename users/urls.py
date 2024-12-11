from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"
 
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reset_password/', views.reset_password_view, name='reset_password')
]