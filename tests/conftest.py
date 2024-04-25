from typing import Any

import pytest
from weather.weather import Unit, WeatherData, WeatherService


@pytest.fixture
def weather_data() -> WeatherData:
    """Return an example weather data object."""
    return WeatherData("Paris", Unit.METRIC, 10.67, 43, 5.14, "clear sky")


@pytest.fixture
def weather_data_dict() -> dict[str, Any]:
    """Example response that could be returned by the OpenWeatherMap API."""
    return {
        "base": "stations",
        "clouds": {"all": 0},
        "cod": 200,
        "coord": {"lat": 48.8534, "lon": 2.3488},
        "dt": 1713800740,
        "id": 2988507,
        "main": {
            "feels_like": 8.92,
            "humidity": 43,
            "pressure": 1023,
            "temp": 10.67,
            "temp_max": 11.71,
            "temp_min": 10,
        },
        "name": "Paris",
        "sys": {
            "country": "FR",
            "id": 2012208,
            "sunrise": 1713761130,
            "sunset": 1713811933,
            "type": 2,
        },
        "timezone": 7200,
        "visibility": 10000,
        "weather": [{"description": "clear sky", "icon": "01d", "id": 800, "main": "Clear"}],
        "wind": {"deg": 10, "speed": 5.14},
    }


@pytest.fixture
def weather_service() -> WeatherService:
    """Return an example WeatherService with a dummy API key."""
    return WeatherService(api_key="TEST")
