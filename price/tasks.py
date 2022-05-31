from json import JSONDecodeError
import logging
import requests
from typing import Optional

from celery import shared_task
from celery.schedules import crontab

from price.models import Symbol, Price
from trackbinance import celery_app

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
    logger.info(f"Retrieving prices for symbols: {symbols}")

    for symbol in symbols:
        price = get_price_from_binance(symbol.name)
        logger.info(f"Price retrieved for symbol {symbol.name}: {price}")

        if not price:
            continue

        price_obj = Price(symbol=symbol, price=price)
        price_obj.save()
        logger.info(f"Price saved for symbol {symbol.name}")

    logger.info("Retrieving finished")


celery_app.conf.beat_schedule = {
    "track_symbols_price": {
        "task": "price.tasks.track_symbols_price",
        "schedule": crontab(minute="*/5"),
    }
}
