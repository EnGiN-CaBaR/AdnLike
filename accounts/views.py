from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse


def validate_username(request):
    username = request.POST.get('register_username', None)
    group = request.POST.get('next', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(), 'group': group
    }
    return JsonResponse(data)


def signup(request):
    if request.method == 'POST':
        username = request.POST['register_username']
        is_taken = User.objects.filter(username__iexact=username).exists()
        if is_taken:
            group = request.POST.get('next', None)
            data = {
                'is_taken': is_taken, 'group': group
            }
            return JsonResponse(data)
        else:
            password = request.POST['register_password']
            password_confirmation = request.POST['password_confirmation']
            if password == password_confirmation:
                try:
                    user = User.objects.get(username=username)
                    return redirect('home')
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username, password=password)
                    user_authenticated = authenticate(username=username, password=password)
                    if user_authenticated is not None:
                        login(request, user_authenticated)
                        data = {
                            'success': True,
                            'redirect_url': '/'
                        }
                        return JsonResponse(data)
            else:
                messages.add_message(request, messages.ERROR, 'Password didn\'t match')
                return redirect('home')
    else:
        return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and password didn\'t match'})
    else:
        return redirect('home')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
