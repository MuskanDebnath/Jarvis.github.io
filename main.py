import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

##speak function will pronounce the string which is passed to it
GIRLIE ="Muskan"

def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function will wish you as per the current time
def wishme():
    hour=int(datetime.datetime.now().hour)
    #print(hour)

    if hour>=0 and hour<12:
        speak("Good morning"+GIRLIE )
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ GIRLIE)
    else:
        speak("Good evening"+ GIRLIE) 
    
    #speak("I am JARVIS.How may I help you?")

#this function will take command from the microphone
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user siad:{query}\n")

    except Exception as e:
        print(f"say that again please{e}")
        query= None 
    return query       


#main program strats here.......
speak("Initializing Jarvis...")
wishme()   
query=takecommand()



##logic for executing tasks as per the quary
if 'wikipedia' in query.lower():
    speak("searching wikipedia...")
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences =2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")   
    #url="youtube.com"
    #chrome_path='C:\Users\DELL\AppData\Local\Google\Chrome\Application'
    
    #webbrowser.get(using='google-chrome').open(url)
