from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import socket
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # Ini bikin /metrics otomatis

hostname = socket.gethostname()

@app.route("/")
def index():
    return f"Hello from {hostname}"

@app.route("/loadtest")
@metrics.counter('loadtest_requests_total', 'Number of loadtest requests')
def loadtest():
    return jsonify({
        "server_hostname": hostname,
        "timestamp": time.time()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
