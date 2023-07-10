from django.urls import path
from .views import register, signin

urlpatterns = [
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
]
