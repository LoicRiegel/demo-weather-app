"""Get weather information for a city specified by the user."""

import os
from typing import Annotated

import typer

from .weather import Unit, WeatherService

API_KEY_ENVIRONMENT_VARIABLE = "OPENWEATHERMAP_KEY"


app = typer.Typer()


def read_api_key(environment_variable: str = API_KEY_ENVIRONMENT_VARIABLE) -> str | None:
    """Return the value of the API Key read as environment variable, or None if the environment variable was not set."""
    return os.getenv(environment_variable)


@app.command()  # type: ignore[misc]
def main(
    city: Annotated[str, typer.Argument(help="The city for which to display the weather forecast")],
    unit: Annotated[Unit, typer.Option(help="Units to use for weather data")] = Unit.METRIC,
) -> int:
    """Entry point of the weather app."""
    api_key = read_api_key()

    if api_key is None:
        print(f"Could not read the API! Please set it in the {API_KEY_ENVIRONMENT_VARIABLE} environment variable.")
        return 1

    weather_service = WeatherService(api_key)

    weather_data = weather_service.get_weather_data(city, unit)
    if weather_data is None:
        print("Failed to get weather information from OpenWeatherMap! Check your internet connection!")
        return 1
    print(weather_data)
    return 0
