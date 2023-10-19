from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<str:id>/', views.event, name='event'),
    path('venue/', views.venue, name='venue'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name="logout"),
    path('bookings/', views.bookings, name="bookings"),
    path('book_event', views.book_event, name='book_event'),
]
