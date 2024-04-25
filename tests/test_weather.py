from typing import Any

import pytest
from weather import weather
from weather.weather import WeatherData, WeatherService


class TestWeatherData:
    """Test the WeatherData class."""

    def test___str__(self, weather_data: WeatherData):
        assert (
            str(weather_data)
            == """Weather for Paris:
  Main weather: clear sky
  Temperature: 10.67 Celsius
  Humidity: 43 %
  Wind speed: 5.14 km/h
"""
        )


class TestWeatherService:
    """Test the WeatherService class."""

    def test_get_weather_data(
        self,
        weather_service: WeatherService,
        weather_data_dict: dict[str, Any],
        weather_data: WeatherData,
        monkeypatch: pytest.MonkeyPatch,
    ):
        class ResponseMock:
            def __init__(self) -> None:
                self.ok = True

            def json(self) -> dict:
                return weather_data_dict

        def get_mock(url: str) -> ResponseMock:  # same signature as the requests.get
            return ResponseMock()

        monkeypatch.setattr(weather.requests, "get", get_mock)
        assert weather_service.get_weather_data("some city") == weather_data

    def test_get_weather_data_response_not_ok(self, weather_service: WeatherService, monkeypatch: pytest.MonkeyPatch):
        class ResponseMock:
            def __init__(self) -> None:
                self.ok = False
                self.status_code = 400

        def get_mock(url: str) -> ResponseMock:  # same signature as the requests.get
            return ResponseMock()

        monkeypatch.setattr(weather.requests, "get", get_mock)
        assert weather_service.get_weather_data("some city") is None

    def test_get_weather_data_response_request_exception_raises(
        self, weather_service: WeatherService, monkeypatch: pytest.MonkeyPatch
    ):
        def get_mock(url: str):
            raise weather.requests.RequestException()

        monkeypatch.setattr(weather.requests, "get", get_mock)
        assert weather_service.get_weather_data("some city") is None
