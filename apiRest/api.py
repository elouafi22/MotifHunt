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
    texteresumer = su.getSummary()

    return jsonify({"text": texteresumer})


app.run(debug=True)
