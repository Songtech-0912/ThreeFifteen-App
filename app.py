from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

original_busdata = {
    "absent": [i for i in range(1, 32)],
    "left_street": [],
    "right_street": [],
    "left_school": [],
    "right_school": []
}

busdata = original_busdata

def generatepwd():
    token = "5fc0ac76f035d603d525d21ecad5d80c"
    pwd = token[3] + token[5] + token[1] + token[-1] + token[8] + token[9] + token[2] + token[-2] + token[7] + token[7] + token[11]
    return pwd

password = {
    "key": generatepwd()
}

@app.route("/")
def main():
    global busdata
    return render_template("main.html", busdata=busdata)

@app.route("/key", methods=["GET"])
@cross_origin()
def get_key():
  global password
  return password

@app.route("/busdata", methods=["GET", "POST"])
@cross_origin()
def transfer_data():
    global busdata
    if request.method == "POST":
      # probably add in a signed integrity check here
      busdata = request.get_json()
    return jsonify(busdata)

if __name__ == "__main__":
    app.run()
