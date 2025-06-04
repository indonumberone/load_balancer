from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import socket
import time

app = Flask(__name__)
hostname = socket.gethostname()

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0', instance=hostname)

@app.route("/")
def index():
    return f"Hello from {hostname}"

@app.route("/loadtest")
@metrics.counter('loadtest_requests_total', 'Number of loadtest requests')
def loadtest():
    time.sleep(0.1)  
    return jsonify({
        "server_hostname": hostname,
        "timestamp": time.time()
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
