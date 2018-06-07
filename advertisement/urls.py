from django.urls import path
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('create_adv/', views.CreateAdvertisement.as_view(), name='create'),
    path('create_adv/publish/<slug:adv_slug_name>/<int:pk>/',
         views.PublishAdvertisement.as_view(), name='publish'),
]
