from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .models import Account


def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('pass')
    if request.method == "POST":
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('username or password is incorrect')

    return render(request, 'signin.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        print(username, email, pass1, pass2)
        my_user = Account.objects.create_user(username, email, pass1)
        my_user.save()
        return redirect('signin')
    return render(request, 'register.html')
