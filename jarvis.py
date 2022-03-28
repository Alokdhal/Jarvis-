import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 and hour == 12:
        speak("Good Morning")

    elif hour >= 12 and hour <= 18:
        speak("good afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis sir! ,How may I help you? ")


def takeCommand():              #it takes microphone  input from user 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"you said : {query}\n")

        except Exception as e:
            return "None"

    return query

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

    if 1:
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open Google' in query:
            webbrowser.open("google.com")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'play music' in query:
            musicDir = "D:\\songs"
            songs = os.listdir(musicDir)
            print(songs)
            os.startfile(os.path.join(musicDir, songs[0]))

        elif 'the time' in query:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,the time is {startTime}")
