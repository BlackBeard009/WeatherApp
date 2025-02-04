import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings


def get_weather(request):
    city = request.GET.get("city", "New York")  # Default city
    api_key = settings.WEATHERAPI_KEY
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()
        weather_info = {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"]
        }
    except Exception:
        weather_info = {"error": "Could not fetch weather data"}

    return JsonResponse(weather_info)


import json

def weather_view(request):
    city = request.GET.get("city", "New York")
    response = get_weather(request)
    data = json.loads(response.content)
    return render(request, "weather/weather.html", {"weather": data})
