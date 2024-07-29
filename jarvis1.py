import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said :(query)\n')
              
    except Exception as e:
        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("yes sir")
            speak("yes sir")
                
                
                