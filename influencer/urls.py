from django.urls import path

from influencer.views import InfAdvertisementList
from . import views

app_name = 'influencer'

urlpatterns = [
    path('', InfAdvertisementList.as_view(), name='ad_recommend_list'),
]
