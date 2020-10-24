#importing necessary libraries.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "Mustafa"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak function will make a.i speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


#this function will make jarvis say "good morning" etc.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER + "...")

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER + "...")
    
    else:
        speak("Good Evening" + MASTER + "...")

    speak("How may I help you?...")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please.")
        query = None
    
    return query


#Jarvis starts from here:
speak("Initializing Jarvis...")
wishMe()
query = takeCommand()


#first task is to search something from wikipedia.
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.get(chrome_path).open("youtube.com")

elif 'open google' in query.lower():
    webbrowser.get(chrome_path).open("google.com")

elif 'time' in query.lower():
    strTime=datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {strTime}")