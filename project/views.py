from django.shortcuts import render
from store.models import Product
from category.models import Category
# from django.contrib.auth.models import User


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


# def register(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         gender = request.POST['gender']
#         city = request.POST['city']
#         country = request.POST['country']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
#
#         print(first_name, last_name, email, gender, city, country, pass1, pass2)
#         my_user = User.objects.create_user(first_name, last_name, email, gender, city)
#         my_user.save()
#         # return redirect('signin')
#     return render(request, 'register.html')


def dashboard(request):
    return render(request, 'dashboard.html')


# def place_order(request):
#     return render(request, 'place_order.html')

def search(request):
    return render(request, 'search_result.html')
