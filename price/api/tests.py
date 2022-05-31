from django.test import TestCase

from price.models import Symbol, Price


class PriceViewSetTestCase(TestCase):
    def setUp(self):
        symbol = Symbol.objects.create(name="BTCUSDT")
        Price.objects.create(symbol=symbol, price=123)

    def test_price_view_set(self):
        resp = self.client.get("/api/price/?symbol=BTCUSDT")
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(resp.content, b"[]")
        resp = self.client.get("/api/price/?symbol=123123")
        self.assertEqual(resp.content, b"[]")
