from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio
import json


SetLogLevel(-1)

def detect_wakeword(wake_word:str):
    model = Model('./vosk-model-small-pt-0.3')
    recognizer = KaldiRecognizer(model, 16000)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    stream.start_stream()
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            texto = result.get("text", "")
            if texto:
                print(texto.lower().split()[:2])
            if texto.lower().split()[:len(wake_word.split())] == wake_word.lower().split():
                print('[Vosk]')

if __name__ == "__main__":
    detect_wakeword('executar comando')
