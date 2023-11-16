import whisper


class transcription:
    "this class for trancripe audio to text"

    def __init__(self, nomAudio, Namemodel="base"):
        self.nomAudio = nomAudio
        self.model = whisper.load_model(Namemodel)

    def execute(self):
        result = self.model.transcribe("/content/audio.mp3")
        result = self.model.transcribe("/content/audio.mp3")
        return result["text"]
