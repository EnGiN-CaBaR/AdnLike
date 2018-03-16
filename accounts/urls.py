from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('signup/influencer', views.influencer_login, name='influencer'),
    path('signup/brand', views.brand_login, name='brand'),
    path('logout/', views.logout_view, name='logout'),
]
