from django.urls import path
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('publish/<slug:slug_name>/<int:pk>/',
         views.PublishAdvertisement.as_view(), name='publish'),
    path('delete/<slug:slug_name>/<int:pk>/',
         views.DeleteAdvertisement.as_view(), name='delete'),
]
