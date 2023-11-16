import flask
from flask import jsonify
from transcripteur import transcription

app = flask.Flask(__name__)


@app.route("/text", methods=["GET"])
def get_text():
    objtranscripteur = transcription()
    text = transcription.execute()
    return jsonify({"text": text})


app.run(debug=True)
