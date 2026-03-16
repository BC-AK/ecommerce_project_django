#register view

from django.shortcuts import render, redirect
from django.contrib.auth.models import User



def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'users/register.html')

#login view

from django.contrib.auth import authenticate, login

def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('product_list')

    return render(request, 'users/login.html')

#logout view

from django.contrib.auth import logout


def user_logout(request):

    logout(request)

    return redirect('login')