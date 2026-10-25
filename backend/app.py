from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "Enterprise Payment Engine",
        "status": "Running"
    })

@app.route("/payment")
def payment():
    return jsonify({
        "payment_status": "SUCCESS",
        "message": "Payment simulated successfully"
    })

@app.route("/notification")
def notification():
    return jsonify({
        "notification_status": "SENT",
        "message": "Payment notification simulated successfully"
    })

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)