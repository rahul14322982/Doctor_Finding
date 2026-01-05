import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-doctor", methods=["POST"])
def get_doctor():
    data = request.json   # data coming from HTML

    url = "https://doctor-finding.onrender.com/predict"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, json=data, headers=headers)

    return jsonify({
        "status": response.status_code,
        "result": response.text
    })


if __name__ == "__main__":
    app.run(debug=True)
