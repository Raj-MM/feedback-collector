from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# In-memory list to store feedback
feedback_items = []


@app.route("/items", methods=["GET"])
def get_feedback():
    return jsonify(feedback_items)


@app.route("/items", methods=["POST"])
def add_feedback():
    data = request.get_json()

    feedback = {
        "id": len(feedback_items) + 1,
        "name": data["name"],
        "message": data["message"],
        "rating": data["rating"]
    }

    feedback_items.append(feedback)

    return jsonify(feedback), 201


@app.route("/health", methods=["GET"])
def health_check():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)