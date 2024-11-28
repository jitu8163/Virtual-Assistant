import pyttsx3
import speech_recognition
import time
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('jituraika8163@gmail.com', 'googlepasscode')
    server.sendmail('jituraika8163@gmail.com', to, content)
    server.close()


def Email():
    try:
        speak("whom should i send")
        to = input()
        speak("What should I say?")
        content = takeCommand()
        sendEmail(to, content)
        speak("Email has been sent !")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")
