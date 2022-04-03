#!/usr/bin/env python3.10
import requests
import json
import datetime

from src.config import WEATHER_URL


def query_city_metadata(city: str) -> dict:
    """

    :param city:
    :return: Where On Earth ID
    """

    url = f"{WEATHER_URL}location/search/"
    parameters = {"query": city}

    return query_api(url, parameters=parameters)[0]


def query_city_forecast(city_woeid: int) -> list:
    """

    :param city_woeid:
    :return:
    """
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    url = f"{WEATHER_URL}location/{city_woeid}/{tomorrow.strftime('%Y/%m/%d')}/"

    return query_api(url)


def query_api(url: str, parameters: dict = None) -> list:
    """

    :param url:
    :param parameters:
    :return:
    """

    response = []

    try:
        response = json.loads(requests
                              .get(url=url, params=parameters)
                              .text)
    except (requests.RequestException, json.decoder.JSONDecodeError) as request_error:
        exit(request_error)

    if len(response) < 1:
        exit("City not found.\nFind your city here : https://www.findmecity.com/")

    return response
