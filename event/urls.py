from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/', views.event, name='event'),
    path('venue/', views.venue, name='venue'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register'),
]
