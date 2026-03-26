import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            print("🌦 Weather Report")
            print("-" * 30)
            print("Temperature:", data["main"]["temp"], "°C")
            print("Condition:", data["weather"][0]["description"])

        elif response.status_code == 429:
            print("⚠️ Rate limit exceeded. Please try later.")

        else:
            print(f"❌ Error: {response.status_code}")

    except Exception as e:
        print("Request failed:", e)


# Do not log user location data (such as city names).
# This follows privacy principles like GDPR (data minimization).

get_weather("Hyderabad")
