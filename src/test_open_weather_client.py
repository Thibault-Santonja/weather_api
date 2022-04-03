import unittest.mock
from unittest import TestCase

import datetime

from src.open_weather_client import resolve_command, get_command_arguments, get_city_tomorrow_forecast
from src.config import WEATHER_STATE


class Test(TestCase):
    def test_resolve_command(self):
        with unittest.mock.patch("sys.argv", ["main", "Geneva"]):
            self.assertIsInstance(resolve_command(), str)
            self.assertIn(resolve_command(), WEATHER_STATE.values())

    def test_get_command_arguments(self):
        with unittest.mock.patch("sys.argv", ["main", "Geneva"]):
            self.assertEqual(get_command_arguments(), {'city': 'Geneva'})

    def test_get_city_tomorrow_forecast(self):
        city_forecast = get_city_tomorrow_forecast("Geneva")
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        self.assertIsInstance(city_forecast, dict)
        self.assertEqual(city_forecast.get('applicable_date'), tomorrow.strftime('%Y-%m-%d'))
