from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/settings/account', views.SettingAccountView.as_view(), name='settings_account'),
    path('<int:pk>/settings/profile', views.SettingProfileView.as_view(), name='settings_profile'),
    path('settings/password/', views.password, name='password'),
]
