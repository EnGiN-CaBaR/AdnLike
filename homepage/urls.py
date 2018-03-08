from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
]
