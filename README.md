# Wallet API Service

This service acts as an API gateway forwarding requests to three different endpoints: Exchange Rates Service, User Identity Service, and Financial Service. It runs on http://localhost:5000.

## Endpoints and Routing

```
SERVERS = {
    'EXCHANGE_RATES_SERVICE': 'http://localhost:8081',
    'IDENTITY_USER_SERVICE': 'http://localhost:8082',
    'FINANCIAL_SERVICE': 'http://localhost:8083',
}

ROUTES = {
    /v1/exchange-rates: SERVERS['EXCHANGE_RATES_SERVICE'],
    /v1/convert: SERVERS['EXCHANGE_RATES_SERVICE'],
    /v1/login: SERVERS['IDENTITY_USER_SERVICE'],
    /v1/register: SERVERS['IDENTITY_USER_SERVICE'],
    /v1/token: SERVERS['IDENTITY_USER_SERVICE'],
    /v1/assets: SERVERS['FINANCIAL_SERVICE'],
    /v1/transactions: SERVERS['FINANCIAL_SERVICE'],
    /v1/balance: SERVERS['FINANCIAL_SERVICE'],
}
```

## How it Works

The service dynamically forwards incoming requests to the respective endpoints based on the route. If the route matches any defined in the ROUTES, it will be redirected accordingly.

```
path = request.path
path = path.rstrip('/')

for route, target_url in ROUTES.items():
    if path.startswith(route):
        target_url = f"{target_url}{request.full_path}"

        response = requests.request(
            method=request.method,
            url=target_url,
            headers=request.headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )

        return response.content, response.status_code, response.headers.items()

return {'error': 'Route not found'}, 404

```

# Makefile

This Makefile provides a set of commands to help with building, running, and managing the Wallet API Service.

## Prerequisites

Before using this Makefile, make sure you have the following dependencies installed:

- Docker

## Usage

Set Environment Variables

Before running the service, ensure that the necessary environment variables are set. These can be configured in the Makefile or directly in your shell.

```
export FLASK_APP=src/app/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_PORT=5000
export PYTHONPATH=$(shell pwd)
```

## Available Commands

- make start: Run the Flask application in development mode.

- make clean: Clean up any cached files (e.g., pycache).

- make build: Build the Docker image for the service.

- make run: Run the Docker container using the built image.

- make stop: Stop and remove the running Docker container.

## Docker Image and Container Naming

```
Docker Image Name: wallet_api_service_image
Docker Container Name: wallet_api_service_container
```

# API Design Documentation

- Wallet Exchange Rate Service API (Component B) - [Swagger File](https://github.com/imdiegolopes/puc-mvp-03-wallet-exchange-rate-service/blob/master/docs/open_api/swagger.yml)
- Wallet Identity Service API (Component C) - [Swagger File](https://github.com/imdiegolopes/puc-mvp-03-wallet-identity-service/blob/master/docs/open_api/swagger.yml)
- Wallet Financial Service API (Component C) - [Swagger File](https://github.com/imdiegolopes/puc-mvp-03-wallet-financial-service/blob/main/docs/open_api/swagger.yml)

# Architecture Diagram

![Image Description](https://i.imgur.com/gJCkvuM.png)

- Component A, B and 2x C represented on this diagram above
