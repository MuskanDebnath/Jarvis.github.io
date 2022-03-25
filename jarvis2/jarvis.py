import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os##for music
import random
import smtplib#for email sending
import socket

socket.getaddrinfo("localhost",8080)
engine=pyttsx3.init('sapi5')##to collect voices....
voices=engine.getProperty('voices')
##there is two voices in laptop one is male "david" another one is female "zira"
#print(voices[1].id)
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good eveing")


    speak("i am jarvis, Muskan. How may i help you?")    
          
def takecommond():
    '''it will hear our command and will try to execute it
    it takes microphone input and string as output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1##it will wait  1 second for us to speak
        audio=r.listen(source)
    try:
        print("recognising......")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please....")
        return "none"
    
    return query

def sendemail(to,content):
    server=smtplib.SMTP("smpt.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("bikasdn68@gmail.com","bikas1968@muskan")
    server.sendemail("bikasdn68@gmail.com",to,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query=takecommond().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia. summary(query,sentences=4)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        # elif "play music" in query: 

        #     pass#must have some directory where you have saved some of your favourate songs in laptop
        #     music_dir=path
        #     songs=os.listdir(music_dir)
        #     print(songs)
        #     #os.startfile(os.path.join(music_dir,songs[random.choice(songs)]))
        #     rdm=random.randint(0,len(songs)-1)
        #     os.startfile(os.path.join(music_dir,songs[rdm]))

        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")

        elif "open code" in query:
            codepath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codepath)  

        # elif "email to" in query:
        #     try:
        #         speak("what should i say")
        #         content=takecommond()
        #         to="manjudn1973@gmail.com"
        #         sendemail(to,content)
        #         speak("Email has been send!")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry, i am not able to send this email at the moment")

        elif "exit" in query:
            exit()        


        
    