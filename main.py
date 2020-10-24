#importing necessary libraries.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

#setting some variables
MASTER = "Your name"
chrome_path = 'Your chrome.exe path'
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

#this function will make jarvis to take commands
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

#it can also open youtube or google by saying "open google" or "open youtube".
elif 'open youtube' in query.lower():
    webbrowser.get(chrome_path).open("youtube.com")

elif 'open google' in query.lower():
    webbrowser.get(chrome_path).open("google.com")

#it can also tell you the time if you ask "what time it is?"    
elif 'time' in query.lower():
    strTime=datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {strTime}")
