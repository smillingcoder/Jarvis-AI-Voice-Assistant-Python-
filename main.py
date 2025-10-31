import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from Searchweather import temperature
from lama3 import lama
from dotenv import load_dotenv
import os
load_dotenv()
brave_path=os.getenv("BRAVE_PATH")
if brave_path and os.path.exists(brave_path):
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
else:
    print("⚠️ Brave browser path not found! Falling back to default browser.")
newsapi=os.getenv("news_api_key")
r=sr.Recognizer()
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def Processcommand(c):
    if "google" in c.lower():
        webbrowser.get("brave").open("https://www.google.com")
    elif "youtube" in c.lower():
        webbrowser.get("brave").open("https://www.youtube.com")
    elif "anime" in c.lower():
        webbrowser.get("brave").open("https://hianime.to/home")
    elif "amazon" in c.lower():
        webbrowser.get("brave").open("https://www.amazon.com")
    elif "play" in c.lower():
        song=c.lower().split()[1]
        link=musiclibrary.music[song]
        webbrowser.get(brave_path).open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data = r.json()
        titles = [article["title"] for article in data.get("articles", [])]
        for i in titles:
            speak(i)     
    elif "weather" in c.lower():
        speak(temperature("vadodara"))
    else:
        speak(lama(c.lower()))
if __name__=="__main__":
    print("Initializing jarvis....")
    speak("Initializing jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,phrase_time_limit=10,timeout=10)
            print("Recognizing...")
            word=r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("yes?")
                print("jarvis active...")
                with sr.Microphone() as source:
                    audio = r.listen(source,phrase_time_limit=10,timeout=5)
                    command=r.recognize_google(audio)
                    print(command)
                    Processcommand(command)
        except Exception as e:
            print("error;{0}".format(e))




      
           
            


