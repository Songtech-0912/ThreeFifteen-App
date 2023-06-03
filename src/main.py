from flask import Flask, jsonify, request
import sys
import json

app = Flask(__name__)
# Some dummy code...
busdata = {
    "Buses present": None
}

@app.route("/")
def main():
    return r"See <a href='/busdata'>busdata/</a> for school bus API"

@app.route("/busdata", methods=["GET", "POST"])
def transfer_data():
    global busdata
    if request.method == "POST":
        busdata = request.get_json()
        return "Got post!\n", 200
    else:
        return jsonify(busdata)

if __name__ == "__main__":
    app.run(debug=True)
