from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts import user_settings
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
        user_group = request.POST.get('next', None)
        if is_taken:
            data = {
                'is_taken': is_taken, 'group': user_group
            }
            return JsonResponse(data)
        else:
            password = request.POST['register_password']
            try:
                user = User.objects.get(username=username)
                return redirect('home')
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                user_settings.add_user_to_group(user, True, user_group)
                user_authenticated = authenticate(username=username, password=password)
                if user_authenticated is not None:
                    login(request, user_authenticated)
                    if user_group == 'brand':
                        data = {
                            'success': True,
                            'redirect_url': 'brand/'
                        }
                    elif user_group == 'influencer':
                        data = {
                            'success': True,
                            'redirect_url': 'influencer/'
                        }
                    else:
                        data = {
                            'success': False,
                            'redirect_url': '/'
                        }
                    return JsonResponse(data)
    else:
        return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(username=username, password=password)
        user_group = user.groups.values_list('name', flat=True).first()
        if user is not None:
            login(request, user)
            if user_group == 'brand':
                data = {
                    'success': True,
                    'redirect_url': 'brand/'
                }
            elif user_group == 'influencer':
                data = {
                    'success': True,
                    'redirect_url': 'influencer/'
                }
            else:
                data = {
                    'success': False,
                    'redirect_url': '/'
                }
            return JsonResponse(data)
        else:
            data = {
                'success': False,
                'message': 'Username or password are not correct!!'
            }
            return JsonResponse(data)
    else:
        return redirect('home')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
