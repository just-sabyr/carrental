"""Defines URL patterns for frontend app"""

from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from frontend.views import CarDetailsView, NewBookingView, HomeView

app_name = 'frontend'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('car/<int:pk>/', CarDetailsView.as_view(), name='car-details'),

    path('booking/<int:car_pk>/', NewBookingView.as_view(), name='new-booking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)