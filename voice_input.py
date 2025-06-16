import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source, timeout=7)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    except sr.WaitTimeoutError:
        return "No speech detected."
