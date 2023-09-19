from handlers.healthcheck_handler import HealthcheckHandler
from handlers.proxy_handlers import ProxyHandler
from flask import (
    Flask,
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule('/', 'index', HealthcheckHandler.handle, methods=['GET'])
app.add_url_rule('/<path:path>', 'proxy', ProxyHandler.handle, methods=['GET', 'POST', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=5000, host="0.0.0.0")
