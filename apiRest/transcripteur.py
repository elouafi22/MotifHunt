import whisper
import os


class transcription:
    "this class for trancripe audio to text"

    def __init__(
        self,
        nomAudio="..\resource\audio.mp3",
        Namemodel="base",
    ):
        self.nomAudio = nomAudio
        if not os.path.exists(self.nomAudio):
            print(f"Le fichier audio {self.nomAudio} n'a pas été trouvé.")
        else:
            print("le fichier existe")
        self.model = whisper.load_model(Namemodel)

    def execute(self):
        result = self.model.transcribe(self.nomAudio)
        return result["text"]


obj = transcription()
obj.execute()
