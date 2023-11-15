import flask
from flask import jsonify

app = flask.Flask(__name__)


@app.route("/text", methods=["POST"])
def get_text():
    text = "bonjour tout le monde"
    return jsonify({"text": text})


app.run(debug=True)
