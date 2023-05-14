from django.shortcuts import render
# Create your views here.


def review_cart(request):
    return render(request, 'place_order.html')


def order(request):
    return render(request, 'order_complete.html')