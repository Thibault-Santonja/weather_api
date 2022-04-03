from unittest import TestCase

import datetime

from src.meta_weather_api import query_city_metadata, query_city_forecast, query_api
from src.config import WEATHER_URL


class Test(TestCase):
    def test_query_city_metadata(self):
        london_metadata = {
            'title': 'London',
            'location_type': 'City',
            'woeid': 44418,
            'latt_long': '51.506321,-0.12714'
        }
        self.assertEqual(query_city_metadata("London"), london_metadata)

        with self.assertRaises(TypeError):
            query_city_metadata()

    def test_query_city_forecast(self):
        city_forecast = query_city_forecast(44418)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        self.assertIsInstance(city_forecast, list)
        self.assertGreater(len(city_forecast), 1)
        self.assertIsInstance(city_forecast[0], dict)
        self.assertEqual(city_forecast[0].get('applicable_date'), tomorrow.strftime('%Y-%m-%d'))

    def test_query_api(self):
        url = f"{WEATHER_URL}location/search/"
        parameters = {"query": "Geneva"}
        expected_response = [
            {
                "title": "Geneva",
                "location_type": "City",
                "woeid": 782538,
                "latt_long": "46.208351,6.142700"
            }
        ]
        self.assertEqual(query_api(url, parameters), expected_response)

        url = f"{WEATHER_URL}location/{expected_response[0].get('woeid')}/2022/04/04/"
        response = query_api(url)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(response[0].get('applicable_date'), "2022-04-04")

    def test_query_api_wrong_url(self):
        with self.assertRaises(SystemExit):
            url = f"{WEATHER_URL}qzkdll/search/"
            query_api(url)

    def test_query_api_wrong_city(self):
        with self.assertRaises(SystemExit):
            url = f"{WEATHER_URL}location/search/"
            parameters = {"query": "Fake York"}
            query_api(url, parameters)
