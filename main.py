import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import cv2
import pywhatkit
import smtplib
import sys
from requests import get

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

#function to talk(text-voice)
def talk(text):
    engine.say(text)
    engine.runAndWait()

#function to take command(voice-text)
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="en-in")
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)        
    except:
        pass
    return command

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("aahilrehman71@gmail.com", "6203181500Ak")
    server.sendmail("aahilrehman71@gmail.com", to, content)
    server.close()

#function to greet
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour  <=12:
        talk("good morning sir. I am alexa . what can I do for you ?")
    elif hour >12 and hour<18:
        talk("good afternoon sir. I am alexa .  what can I do for you ?")
    else:
        talk("good evening sir. I am alexa .  what can I do for you ?")

def run_alexa():
    command = take_command()
    print(command)
    if "play " in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info1 = wikipedia.summary(person, 1)
        print(info1)
        talk(info1)
    elif "what is" in command:
        item = command.replace("what is", "")
        info2 = wikipedia.summary(item, 1)
        print(info2)
        talk(info2)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "good morning" in command:
        talk("good morning sir. I am alexa . what can I do for you ?")
    elif "good afternoon" in command:
        talk("good afternoon sir. I am alexa .  what can I do for you ?")
    elif "good evening" in command:
        talk("good evening sir. I am alexa .  what can I do for you ?")
    elif "google" in command:
        webbrowser.open("google.com")
    elif "facebook" in command:
        webbrowser.open("www.facebook.com")
    elif "instagram" in command:
        webbrowser.open("www.instagram.com")
    elif "search" in command:
        talk("sir, what can I search for you")
        cm = take_command().lower()
        webbrowser.open(f"{cm}")
    elif "send message" in command:
        talk("sir, tell me number where you want to send message")
        pno = take_command().lower()
        talk("sir, what do want to say")
        msg = take_command().lower()
        hr = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        pywhatkit.sendwhatmsg(f"+91{pno}", f"{msg}", hr, minute)
    elif "send email" in command:
        try:
            talk("Please tell me email id to send, sir ")
            to = take_command().lower
            talk("what should I say")
            content = take_command().lower
            sendEmail(to, content)
            talk(f"email has been sended to {to}")
        except Exception as e:
            print(e)
            talk("sorry sir , message couldnot send")
    elif "notepad " in command:
        npath = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(npath)
    elif "command prompt" in command:
        os.system("start cmd")
    elif "camera" in command:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow("webcam", img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif "ip address" in command:
        ip = get("https://api.ipify.org").text
        talk(f"your IP address is {ip}")
    elif "close" in command:
        talk("thanks for using me sir, have a good day. closing.....")
        sys.exit()
    else:
        talk("sorry sir i didn't get it. please say it again")


if __name__ == "__main__":
    wish()
    while True:
        run_alexa()
        
       