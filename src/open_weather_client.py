#!/usr/bin/env python3.10
import argparse

from src.meta_weather_api import query_city_forecast, query_city_metadata

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def resolve_command() -> str:
    """

    :return:
    """
    arguments = get_command_arguments()
    city_forecast = get_city_tomorrow_forecast(arguments.get("city"))

    return city_forecast.get('weather_state_name')


def get_command_arguments() -> dict:
    """
    Returns the weather of a given city.

    :return:
    """
    parser = argparse.ArgumentParser(usage="""main.py CITY [OPTIONS]
        Returns the tomorrow weather of a given city.""")
    parser.add_argument('city', help="Wanted city's weather.")

    return vars(parser.parse_args())


def get_city_tomorrow_forecast(city: str) -> dict:
    """

    :param city:
    :return:
    """
    city = query_city_metadata(city)
    city_forecast = query_city_forecast(city.get("woeid"))[0]

    print(f"Tomorrow at {city.get('title')}, you will have {city_forecast.get('weather_state_name').lower()}.")
    return city_forecast
