from doctest import master
from unittest import result
from xmlrpc.client import DateTime
import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr
audio = sr.Recognizer
import datetime as dt
dt.datetime 
import wikipedia as wp
wp.wikipedia
import webbrowser as wb
wb
import subprocess as sb
sb
import os as os
os
import smtplib as s
s

print("initializing jarvis")

MASTER = "FAJAR"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


#speak

def speak(text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(dt.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("morning" + MASTER)
    elif hour >=12 and hour <18:
        speak("afternoon" + MASTER)
    else:
        speak ("evening" + MASTER)
        speak ("")

#micropon
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en")
        print(f"user said: {query}\n")

    except Exception as e:

        print("say that again please")
        return "None"
        
    return query

#mainprogram dimulai di sini
speak("hello my name is ana, can i help you sir")
wishMe()
query = takeCommand()

#logic for taks as per query
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wp.summary(query, sentences=2)
    print(results)
    speak(results)

if "open youtube" in query.lower():
    url = "youtube.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)

elif "open google" in query.lower():
    url = "google.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)

elif "open my website" in query.lower():
    url = "http://localhost/upload/"
   # xampp ="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\XAMPP %s"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)

