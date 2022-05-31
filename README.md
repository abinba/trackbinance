# trackbinance

## The task:

Write a simple API that is tracking a symbol (eg. ETHUSDT or BTCUSDT)price using the binance API.
 
1. User can define symbols through Django admin.
2. The app is fetching data about any given symbol from binance API every 5 minutes [https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT](https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT)
3. App exposes simple endpoint api/price/?symbol=<symbol>
that returns previously fetched data.


## Table of contents:

- health_check
- price - main logic goes here
- trackbinance - configuration of the project
- scripts - where entrypoint is located
- .env.dev - development environment variables
- .flake8 - flake8 configuration
- docker-compose.yml
- Dockerfile
- manage.py
- poetry.lock
- pyproject.toml


## How to Install and Run the project

1) Configure your environment variables in `.env.dev`.
2) `docker-compose up`
3) Create a superuser by `docker exec -it {container_id} python manage.py createsuperuser`
4) Add Symbols in Django admin
5) Go to `api/price/?symbol=YOURSYMBOL` and see the results for past time.
