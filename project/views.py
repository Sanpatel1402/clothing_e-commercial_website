from django.shortcuts import render
from store.models import Product
from category.models import Category


# Create your views here.

# def home(request):
#     products = Product.objects.all().filter(is_available=True)
#     categories = Category.objects.all()
#     context = {'products': products, 'categories': categories}
#     return render(request, 'home.html', context)


# def product(request):
#     return render(request, 'product_detail.html')


def home(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'categorys': categorys,
    }
    return render(request, 'home.html', context)


def signin(request):
    return render(request, 'signin.html')


def register(request):
    return render(request, 'register.html')


def dashboard(request):
    return render(request, 'dashboard.html')


# def place_order(request):
#     return render(request, 'place_order.html')

def search(request):
    return render(request, 'search_result.html')