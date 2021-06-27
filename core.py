import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Welcome back master. I'm Alfred.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube ' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open myanimelist' in query:
            webbrowser.open("https://myanimelist.net/")

        elif 'play music' in query:
            music_dir = "E:\\BOOKS\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.strftime("%H:%M:%S")
            speak(f" The time is {strTime}")

        elif 'open vscode' in query:
            codepath = "E:\\Visual Studio Code\\Code.exe"
            os.startfile(codepath) 

        elif 'open steam' in query:
            codepath = "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam"
            os.startfile(codepath)
        elif 'open epic games' in query:
            codepath = "E:\\Visual Studio Code\\Code.exe"
            os.startfile(codepath)
        elif 'open e drive' in query:
            codepath = "E:"
            os.startfile(codepath)
        elif 'open c drive' in query:
            codepath = "C:"
            os.startfile(codepath)
        elif 'open Battlefield' in query:
            codepath = "E:\\AGFY-Battlefield.4\\AGFY-Battlefield.4\\Battlefield.4\\Battlefield 4\\bf4.exe"
            os.startfile(codepath)
        
        
                

        