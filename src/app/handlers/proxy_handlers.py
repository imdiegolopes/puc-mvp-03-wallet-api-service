from flask import jsonify, request
import requests

class ProxyHandler:
    def __init__():
        pass

    def handle(path):
        SERVERS = {
            'EXCHANGE_RATES_SERVICE': 'http://localhost:8081',
            'IDENTITY_USER_SERVICE': 'http://localhost:8082',
            'FINANCIAL_SERVICE': 'http://localhost:8083',
        }

        ROUTES = {
            # Exchange Rates Endpoints
            '/v1/exchange-rates': SERVERS['EXCHANGE_RATES_SERVICE'],
            '/v1/convert': SERVERS['EXCHANGE_RATES_SERVICE'],
            # User Identity Endpoints
            '/v1/login': SERVERS['IDENTITY_USER_SERVICE'],
            '/v1/register': SERVERS['IDENTITY_USER_SERVICE'],
            '/v1/token': SERVERS['IDENTITY_USER_SERVICE'],
            # Financial Endpoints
            '/v1/assets': SERVERS['FINANCIAL_SERVICE'],
            '/v1/transactions': SERVERS['FINANCIAL_SERVICE'],
            '/v1/balance': SERVERS['FINANCIAL_SERVICE'],
        }
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

        return jsonify({'error': 'Route not found'}), 404
