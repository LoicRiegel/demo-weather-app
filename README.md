# Weather app (demo project)

This demo weather app

## Install

```sh
git clone
cd weather
pip install .
```

## Usage

```
Usage: weather [OPTIONS] CITY

Arguments:
*    city       TEXT                The city for which to display the weather forecast [default: None] [required]
Options:
*  --unit       [metric|imperial]   Units to use for weather data [default: metric]
*  --help                           Show this message and exit.
```

This app uses [OpenWeatherMap](https://openweathermap.org) service to fetch the weather information. To use this app, you first need to create a personal API key (see [here](https://openweathermap.org/appid)).

Do once:
```sh
export OPENWEATHERMAP_KEY=<YOUR_API_KEY>
```

Then:
```sh
weather --help
weather London
weather London --unit metric
```

## Contributing

Use **pre-commit hooks** which will run the ``ruff`` linter and formatter, and run the ``mypy`` type-checker:
```sh
pre-commit install
```

### Run unit tests

```sh
pytest
```
