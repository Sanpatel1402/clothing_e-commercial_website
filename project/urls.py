from django.urls import path
from .views import home, signin, register, dashboard, search

urlpatterns = [
    path('', home, name='home'),
    path('signin/', signin, name='signin'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('search/', search, name='search'),
]
