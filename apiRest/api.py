import flask
from flask import jsonify
from transcripteur import transcription
from sumarizer import summarizer

app = flask.Flask(__name__)


@app.route("/text", methods=["GET"])
def get_text():
    objtranscripteur = transcription()
    text = objtranscripteur.execute()
    su = summarizer(text)
    return jsonify({"text": su.getSummary()})


app.run(debug=True)
