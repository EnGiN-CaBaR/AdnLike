from django.urls import path
from . import views

app_name = 'brand'

urlpatterns = [
    path('', views.BrandHomePage.as_view(), name='brand_home'),
]