from django.urls import path
from .views import home, dashboard, search

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('search/', search, name='search'),
]
