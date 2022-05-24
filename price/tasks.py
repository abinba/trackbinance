import logging
from json import JSONDecodeError
from typing import Optional
import requests

from celery import shared_task
from celery.schedules import crontab

from trackbinance import celery_app
from price.models import Symbol, Price

logger = logging.getLogger(__name__)


def get_price_from_binance(symbol_name: str) -> Optional[float]:
    symbol_data = requests.get(
        "https://api.binance.com/api/v3/avgPrice",
        params={
            "symbol": symbol_name,
        },
    )
    try:
        symbol_data = symbol_data.json()
    except JSONDecodeError as e:
        logger.error(
            f"Exception raised while converting binance data from JSON: {e}, symbol: {symbol_name}"
        )
        return None

    if "price" not in symbol_data:
        logger.error(
            f"Exception raised while trying to get the price, symbol: {symbol_name}, response: {symbol_data}"
        )
        return None

    price = float(symbol_data["price"])
    return price


@shared_task
def track_symbols_price():
    symbols = Symbol.objects.all()
    for symbol in symbols:
        price = get_price_from_binance(symbol.name)
        if not price:
            continue
        price_obj = Price(symbol=symbol, price=price)
        price_obj.save()


celery_app.conf.beat_schedule = {
    "track_symbols_price": {
        "task": "tasks.track_symbols_price",
        "schedule": crontab(minute="*/5"),
    }
}
