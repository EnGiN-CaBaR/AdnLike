from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.messages import get_messages

from social_django.models import UserSocialAuth


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'homepage/home.html')
    else:
        if request.user.groups.all()[0].name == 'influencer':
            return redirect('influencer:ad_recommend_list')
        elif request.user.groups.all()[0].name == 'brand':
            pass
        else:
            return render(request, 'homepage/home.html')


def error(request):
    # storage = get_messages(request)
    # for message in storage:
    #     if 'social-auth' in message.tags and 'error' in message.level_tag:
    return render(request, 'homepage/error.html')


@login_required
def settings(request):
    user = request.user

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'homepage/settings.html', {
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('homepage:settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'homepage/password.html', {'form': form})
