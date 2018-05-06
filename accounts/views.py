from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from AdnLike import urls


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password == password_confirmation:
            try:
                user = User.objects.get(username=username)
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                user_authenticated = authenticate(username=username, password=password)
                if user_authenticated is not None:
                    login(request, user_authenticated)
                    return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')


def login_user(request):
    return render(request, 'accounts/login.html')


def influencer_login(request):
    return render(request, 'accounts/influencer.html', context={'user_type': 'influencer'})


def brand_login(request):
    return render(request, 'accounts/brand.html', context={'user_type': 'brand'})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'][:-1])
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
