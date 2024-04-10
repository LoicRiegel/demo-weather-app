"""Get weather information for a city specified by the user."""

from enum import Enum
from typing import NamedTuple

import requests


class Unit(Enum):  # TODO: use StrEnum
    """The possible units for weather data."""

    METRIC = "metric"
    IMPERIAL = "imperial"


class WeatherData(NamedTuple):
    """Weather data."""

    location: str
    unit: Unit
    temperature: float
    humidity: float
    wind_speed: float
    description: str = ""

    def __str__(self) -> str:
        return f"""Weather for {self.location}:
  Main weather: {self.description}
  Temperature: {self.temperature} Celsius
  Humidity: {self.humidity} %
  Wind speed: {self.wind_speed} {"km/h" if self.unit == Unit.METRIC else "miles/h"}
"""


class WeatherService:
    """Fetch weather data from the OpenWeatherMap service."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_weather_data(self, city: str, unit: Unit = Unit.METRIC) -> WeatherData | None:
        """Retrieve the latest weather data for a given city in the given unit."""
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={unit.value}"
        try:
            resp = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
        if not resp.ok:
            print(f"Unsuccessful response! Status code {resp.status_code}")
            return None
        data = resp.json()
        return WeatherData(
            location=data["name"],
            description=data["weather"][0]["description"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            unit=unit,
        )
