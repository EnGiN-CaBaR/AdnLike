from django.urls import path
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('adv_summary/', views.summary, name='adv_summary'),
    path('create_adv/', views.create_adv, name='create_adv'),
]
