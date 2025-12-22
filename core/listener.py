import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    path = "temp.wav"
    with open(path, "wb") as f:
        f.write(audio.get_wav_data())

    return path
