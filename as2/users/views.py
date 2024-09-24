from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, 'users/index.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect(reverse('users:index'))
            if not user.is_superuser:
                return HttpResponseRedirect(reverse('users:index'))
            else:
                return redirect('/admin/')
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged out'
    })
