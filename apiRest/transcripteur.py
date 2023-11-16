import whisper


class transcription:
    "this class for trancripe audio to text"

    def __init__(self, nomAudio="/content/audio.mp3", Namemodel="base"):
        self.nomAudio = nomAudio
        self.model = whisper.load_model(Namemodel)

    def execute(self):
        result = self.model.transcribe(self.nomAudio)
        return result["text"]
