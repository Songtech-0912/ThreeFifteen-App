from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import sys
import json
from time import sleep

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

original_busdata = {
    "present": [],
    "absent": [i for i in range(1, 32)]
}

busdata = original_busdata

@app.route("/")
def main():
    global busdata
    return render_template("main.html", busdata=busdata)

@app.route("/busdata", methods=["GET", "POST"])
@cross_origin()
def transfer_data():
    global busdata
    return jsonify(busdata)

@app.route("/admin", methods=["GET", "POST"])
def template():
    global busdata
    present = []
    absent = []
    # When the form is submitted, adjust
    # busdata correspondingly
    if request.method == "POST":
        for i in range(1, 32):
            if f"bus-{i}" in request.form:
                present.append(i)
            else:
                absent.append(i)
        busdata["present"] = present
        busdata["absent"] = absent
    # Assemble checkbox data from busdata
    checkbox_data = {}
    for bus in busdata["present"]:
        checkbox_data[bus] = False
    for bus in busdata["absent"]:
        checkbox_data[bus] = True
    # Sort checkbox data so it is in the right order
    checkbox_data = dict(sorted(checkbox_data.items()))
    return render_template("admin.html", busdata=busdata, checkbox_data=checkbox_data)

if __name__ == "__main__":
    app.run(debug=True)
