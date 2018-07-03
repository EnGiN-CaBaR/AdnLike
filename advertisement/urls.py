from django.urls import path
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('', views.BrandAdvertisementCreatePublishPage.as_view(), name='create'),
    path('publish/<slug:adv_slug_name>/<int:pk>/',
         views.PublishAdvertisement.as_view(), name='publish'),
    path('edit/<slug:adv_slug_name>/<int:pk>/',
         views.UpdateAdvertisement.as_view(), name='update'),
]