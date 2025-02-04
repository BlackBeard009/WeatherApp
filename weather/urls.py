from django.urls import path
from .views import get_weather, weather_view

urlpatterns = [
    path("", weather_view, name="home"),  # Displays the weather page
    path("weather/", get_weather, name="weather"),  # Returns weather JSON
]
