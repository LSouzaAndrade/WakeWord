import speech_recognition as sr


def detect_wakeword(wake_word:str):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = recognizer.listen(source)
                texto = recognizer.recognize_google(audio, language="pt-BR")
                print(texto.lower().split()[:2])
                if texto.lower().split()[:len(wake_word.split())] == wake_word.lower().split():
                    print('[SpeechRecognition]')
            except sr.UnknownValueError:
                continue

if __name__ == "__main__":
    detect_wakeword('executar comando')

