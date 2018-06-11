from django.conf.urls import url
from django.urls import path, include
from . import views
from homepage.urls import views as vw

app_name = 'advertisement'

urlpatterns = [
    path('create/', views.CreateAdvertisement.as_view(), name='create'),
    path('publish/<slug:adv_slug_name>/<int:pk>/',
         views.PublishAdvertisement.as_view(), name='publish'),
    path('edit/<slug:adv_slug_name>/<int:pk>/',
         views.UpdateAdvertisement.as_view(), name='update'),
]
