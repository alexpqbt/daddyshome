import speech_recognition as sr
import time

recognizer = sr.Recognizer()

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_sphinx(audio)
        print(text)
    except sr.UnknownValueError:
        print("No understand")

def main():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)

    stop_listening = recognizer.listen_in_background(source, callback)

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        stop_listening()

if __name__ == "__main__":
    main()
