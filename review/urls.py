from django.urls import path
from .views import review_cart, order

urlpatterns = [
    path('review/', review_cart, name='review'),
    path('order/', order, name='order'),
]