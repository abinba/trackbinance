from django.test import TestCase

from price.models import Symbol, Price
from price.tasks import get_price_from_binance, track_symbols_price


class SymbolTestCase(TestCase):
    def setUp(self):
        Symbol.objects.create(name="BTCUSDT")
        Symbol.objects.create(name="ETHUSDT")

    def test_symbols_str(self):
        btcusdt = Symbol.objects.get(name="BTCUSDT")
        ethusdt = Symbol.objects.get(name="ETHUSDT")
        self.assertEqual(str(btcusdt), "Symbol - BTCUSDT")
        self.assertEqual(str(ethusdt), "Symbol - ETHUSDT")


class PriceTestCase(TestCase):
    def setUp(self):
        symbol = Symbol.objects.create(name="BTCUSDT")
        Price.objects.create(symbol=symbol, price=123)

    def test_price(self):
        symbol = Symbol.objects.get(name="BTCUSDT")
        prices = Price.objects.filter(symbol=symbol)
        self.assertEqual(len(prices), 1)
        self.assertEqual(
            str(prices[0]),
            f"Price of symbol: BTCUSDT created at: {prices[0].created_at} is: 123.0",
        )


class TasksTestCase(TestCase):
    def setUp(self):
        Symbol.objects.create(name="BTCUSDT")
        Symbol.objects.create(name="ETHUSDT")

    def test_get_symbol_from_binance(self):
        btcusdt = get_price_from_binance("BTCUSDT")
        self.assertEqual(type(btcusdt), float)
        ethusdt = get_price_from_binance("ETHUSDT")
        self.assertEqual(type(ethusdt), float)
        not_existent_symbol = get_price_from_binance("DOESNOTEXIST")
        self.assertEqual(not_existent_symbol, None)
        no_data = get_price_from_binance("")
        self.assertEqual(no_data, None)

    def test_track_symbols_price(self):
        track_symbols_price()

        self.assertEqual(Price.objects.all().count(), 2)
        self.assertEqual(Price.objects.all().first().symbol.name, "BTCUSDT")
        self.assertEqual(Price.objects.all().last().symbol.name, "ETHUSDT")
