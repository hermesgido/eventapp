from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('event/<str:id>/', views.event, name='event'),
    path('venue/<str:id>/', views.venue, name='venue'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name="logout"),
    path('bookings/', views.bookings, name="bookings"),
    path('bookings_venue/', views.bookings_venue, name="bookings_venue"),
    path('book_event', views.book_event, name='book_event'),
    path('book_venue', views.book_venue, name='book_venue'),
    path('cancel_book_event', views.cancel_book_event, name='cancel_book_event'),
    path('cancel_book_venue', views.cancel_book_venue, name='cancel_book_venue'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

