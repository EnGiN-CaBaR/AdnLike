from django.forms import ModelForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


class SettingsAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class SettingsProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['country', 'city', 'birthday', 'gender', ]