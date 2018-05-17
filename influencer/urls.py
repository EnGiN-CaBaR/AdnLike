from django.urls import path
from . import views

app_name = 'influencer'

urlpatterns = [
    path('', views.ad_recommend_list, name='ad_recommend_list'),
]
