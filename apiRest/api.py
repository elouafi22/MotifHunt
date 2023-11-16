import flask
from flask import jsonify
from transcripteur import transcription

app = flask.Flask(__name__)


@app.route("/text", methods=["GET"])
def get_text():
    objtranscripteur = transcription("../resource/audio.mp3")
    text = transcription.execute()
    return jsonify({"text": text})


app.run(debug=True)
