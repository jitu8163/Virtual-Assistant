import pyttsx3
import datetime
import time as tt
import speech_recognition as sr
import smtplib
from secret import senderemail, epwd
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import subprocess as sp
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import string
import random
import cv2
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
import keyboard
import imdb
import wolframalpha

# Initialize pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize speech recognition
r = sr.Recognizer()

# Initialize TF-IDF vectorizer for improved query understanding
vectorizer = TfidfVectorizer()
responses = ["Hello, how can I help you?",
             "I'm sorry, I didn't understand that.", "Here's what I found:"]
vectorizer.fit(responses)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


listening = 'False'


def start_listening():
    global listening
    listening = True
    print('Started Listening')


def pause_listening():
    global listening
    listening = False
    print('Paused Listening')


keyboard.add_hotkey('ctrl+alt+s', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)

# To change the Vice of Model


def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak('Hello this is Jarvis')
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak('Hello this is Friday')


# Greeting function.
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak(' Good morning sir')
    elif hour >= 13 and hour < 18:
        speak(' Good afternoon Sir ')
    elif hour >= 19 and hour < 24:
        speak(' Good evening sir')
    elif hour >= 1 and hour < 6:
        speak(' Good night sir')


# date and time
def time():
    Time = datetime.datetime.now().strftime(
        "%I:%M:%S")  # Hour = I, Minute = M, Second = S
    speak("The current time is: ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(("The current date is: ", date, month, year))


# Wishes on initialization
def wishme():
    speak(greeting())
    # speak(' Welcome back ')
    # speak(' Jarvish at your service sir. Tell me how may i help you.')
    # time()
    # speak('And')
    # date()

# Input taken by the model through user using voice.


def voiceCommand():
    # r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speak("I didn't catch that. Could you please repeat")
        return 'None'
    return query


# To send an Email
def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['from'] = senderemail
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


# To send an whatsapp Message
def sendWhatsmsg(ph_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+ph_no+'&test'+Message)
    sleep(10)
    pyautogui.press()
    pyautogui.press('enter')


def take_picture():
    speak("Opening camera to take a picture.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Error: Could not open camera.")
        return

    # Wait for the camera to initialize and adjust light levels
    for i in range(30):
        cap.read()

    speak("Camera ready. Say 'capture' when you're ready to take the picture.")

    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Error: Failed to capture image.")
            break

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            speak("Camera closed without taking a picture.")
            break

        command = voiceCommand().lower()
        if 'capture' in command:
            cv2.imshow('Captured Image', frame)
            cv2.waitKey(1000)
            cv2.destroyWindow('Camera')

            speak("Picture taken. Do you want to save it?")
            save_response = voiceCommand().lower()

            if any(word in save_response for word in ['yes', 'save', 'okay', 'sure']):
                save_folder = 'pictures'
                if not os.path.exists(save_folder):
                    os.makedirs(save_folder)

                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f'captured_image_{timestamp}.jpg'
                save_path = os.path.join(save_folder, filename)

                cv2.imwrite(save_path, frame)
                speak(f"Image saved as {filename}")
            else:
                speak('Image not saved.')

            break

    cap.release()
    cv2.destroyAllWindows()


# def face_recognition():
#     speak("Opening camera for face recognition.")
#     face_cascade = cv2.CascadeClassifier(
#         cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, img = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#         cv2.imshow('Face Recognition', img)

#         speak("Press q to quit")
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     if len(faces) > 0:
#         speak("Face detected. Do you want to save this blueprint?")
#         response = voiceCommand().lower()
#         if any(word in response for word in ['yes', 'save it', 'obviously', 'yes dude', 'why not', 'sure']):
#             speak("What's the name of this person?")
#             name = voiceCommand()
#             face_img = img[y:y+h, x:x+w]
#             cv2.imwrite(f'{name}_face.jpg', face_img)
#             speak(f"Face blueprint saved as {name}_face.jpg")
#     else:
#         speak("No face detected in the frame.")


def searchgoogle():
    search = voiceCommand()
    speak('What should i search? ')
    wb.open('https://www.google.com/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key='290943b21aa24be3bb1dd38c87a27ec6')
    speak('On which topic you want news')
    topic = voiceCommand()
    data = newsapi.get_top_headlines(q='topic',
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x, y in enumerate(newsdata):
        print(f'{x}{y['description']}')
        speak((f'{x}{y['description']}'))
    speak("Thats it for now. I'll update in some time")


def screenshot():
    name_img = tt.time()
    name_img = 'C:\\Users\\Dell\\OneDrive\\Desktop\\EDU Projects\\Jarvis\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def passwordgen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    pas = (''.join(s[0:passlen]))
    print(pas)
    speak('Password generated')
    speak('Password is {}'.format(pas))


def play_on_youtube(query):
    speak(f"Searching for {query} on YouTube")
    try:
        pywhatkit.playonyt(query)
        speak(f"Playing {query} on YouTube")
    except Exception as e:
        speak("An error occurred while trying to play the video")
        print(e)


def txt2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


    # Main Function
if __name__ == '__main__':
    getvoices(0)
    # wishme()
    speak("Welcome back  sir.")
    # speak('Jarvis at your service. Tell me how may I assist you today.')
    wakeword = 'jarvis'
    while True:
        query = voiceCommand().lower()
        query = word_tokenize(query)
        print(query)
        if listening:
            if wakeword in query:
                if 'time' in query:
                    time()
                elif 'date' in query:
                    date()
                elif 'ram ram' in query:
                    speak('Jay Shree Ram')

                elif 'radhe radhe' in query:
                    speak('Radhe Radhe ji')

                elif 'jay shree shyam' in query:
                    speak('Jay Shree shyam')

                elif 'jay mata di' in query:
                    speak('Jay ho')

                elif 'open CMD' or 'command prompt' in query:
                    speak('Opening command prompt')
                    os.system('start cmd')

                elif 'open camera' in query:
                    speak('opening camera')
                    os.run('start microsoft.windows.camera:', shell=True)

                elif 'play on youtube' in query or 'search on youtube' in query:
                    speak("What would you like to watch on YouTube?")
                    video_query = voiceCommand().lower()
                    play_on_youtube(video_query)

                elif 'open google' in query:
                    wb.open('https://www.google.com')
                    speak('Opening Google')

                elif 'camera' in query:
                    take_picture()
                # elif 'recognise face' in query:
                    # face_recognition()

                elif 'open facebook' in query:
                    wb.open('https://www.facebook.com')
                    speak('Opening Facebook')

                elif 'open instagram' in query:
                    wb.open('https://www.instagram.com')
                    speak('Opening Instagram')

                elif 'open twitter' in query:
                    wb.open('https://www.twitter.com')
                    speak('Opening Twitter')

                elif 'open linkedin' in query:
                    wb.open('https://www.linkedin.com')
                    speak('Opening Linkedin')

                elif 'open github' in query:
                    wb.open('https://www.github.com')
                    speak('Opening Github')

                elif 'open code' in query:
                    codepath = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                    speak('Opening Visual Studio Code')
                    os.startfile(codepath)

                elif 'open pycharm' in query:
                    codepath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe'
                    speak('Opening Pycharm')
                    os.startfile(codepath)

                elif 'open zoom' in query:
                    codepath = 'C:\\Users\\Dell\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                    speak('Opening Zoom')
                    os.startfile(codepath)

                elif 'open telegram' in query:
                    codepath = 'C:\\Users\\Dell\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'
                    speak('Opening Telegram')
                    os.startfile(codepath)

                elif 'open word' in query:
                    codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
                    speak('Opening Microsoft Word')
                    os.startfile(codepath)

                elif 'open excel' in query:
                    codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
                    speak('Opening Microsoft Excel')
                    os.startfile(codepath)

                elif 'open powerpoint' in query:
                    codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
                    speak('Opening Microsoft PowerPoint')
                    os.startfile(codepath)

                elif 'open outlook' in query:
                    codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'
                    speak('Opening Microsoft Outlook')
                    os.startfile(codepath)

                elif 'open onenote' in query:
                    codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE'
                    speak('Opening Microsoft OneNote')
                    os.startfile(codepath)

                elif 'email' in query:
                    speak('To whom you want to send the mail?')
                    receiver_add = input('Email Address of Receiver')
                    speak('What is the subject of the mail?')
                    subject = voiceCommand().capitalize()
                    speak('Please tell me the Message')
                    content = voiceCommand().capitalize()
                    if sendEmail(receiver_add, subject, content):
                        speak('Email has been sent')
                        print('Email has been sent')
                    else:
                        speak('Unable to send the Email. Please Check the erro box')

                elif 'who are you' in query:
                    speak(
                        'I am your virtual assistant. You can call me JARVIS i was created by Jitendra Raika. You can call him JEETU')

                elif 'what can you do' in query:
                    speak('I can send emails, tell you the time, date, and take notes')

                elif 'message' in query:
                    user_name = {
                        'Jarvis': '7976202595',
                        'Sajjan': '9057532707'

                    }
                    try:
                        speak('To whom you want to send the whatsapp message?')
                        name = voiceCommand()
                        ph_no = user_name[name]
                        speak('What is the Message?')
                        message = voiceCommand()
                        sendWhatsmsg(ph_no, message)
                        speak('Message has been sent')
                        speak('Please tell me the content of the note')
                        content = takeCommandCMD()
                        speak('Note saved')
                    except Exception as e:
                        print(e)
                        speak('unable to send the Message')

                elif 'Search for the topic' in query:
                    speak('How many lines you want on this topic?')
                    k = int(voiceCommand())
                    speak('Searching on wikipedia')
                    query = query.replace('wikipedia', '')
                    results = wikipedia.summary(query, sentences=k)
                    speak('According to wikipedia')
                    print(results)
                    speak(results)

                elif 'google' in query:
                    speak('Searching on google')
                    searchgoogle()
                    speak('Here are the results check the google window')
                    # query = query.replace('google', '')

                elif 'weather' in query:
                    speak('For which city you want to check the weather')
                    city = voiceCommand()
                    url = f'https://api.openweathermap.org/data/2.5/weather?q={
                        city}&units=imperial&appid=3b853152cc0e63f319361c76b1c80c5d'
                    res = requests.get(url)
                    data = res.json()
                    weather = data['weather'][0]['main']
                    temp = data['main']['temp']
                    desp = data['weather'][0]['description']
                    temp = round((temp-32)*5/9)
                    print(weather)
                    print(temp)
                    print(desp)
                    speak(f'Weather in {city} is like')
                    speak('Temperature :{} degree celsius '.format(temp))
                    speak('Weather is {}'.format(desp))

                elif 'news' in query:
                    news()

                elif 'open notepad' in query:
                    codepath = 'C:\\Windows\\notepad.exe'
                    speak('Opening Notepad')
                    os.startfile(codepath)

                elif 'open chrome' in query:
                    codepath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                    speak('Opening Chrome Browser')
                    os.startfile(codepath)

                elif 'open drive' in query:
                    codepath = 'C:\\Program Files\\Google\\Drive File Stream\\97.0.1.0\\GoogleDriveFS.exe'
                    speak('Opening Google Drive')
                    os.startfile(codepath)

                # elif 'open ' in query:
                #     os.system('explorer c://{}'.format(query.replace('Open', '')))

                elif 'open Whatsapp' in query:
                    # Open the Start menu
                    pyautogui.press('win')

                    pyautogui.typewrite('WhatsApp')

                    speak('Opening Whatsapp')
                    time.sleep(2)

                    pyautogui.click()

                elif 'read' in query:
                    txt2speech()

                elif 'joke' in query:
                    speak(pyjokes.get_joke())

                elif 'screenshot' in query:
                    screenshot()

                elif 'remember' in query:
                    speak('What should i remember?')
                    data = voiceCommand()
                    speak('You said me to remember that' + data)
                    remember = open('data.txt', 'w')
                    remember.write(data)
                    remember.close()
                elif 'do you know anything' in query:
                    remember = open('data.txt', 'r')
                    speak('You told me to remember that' + remember.read())

                elif 'Generate Password' in query:
                    passwordgen()
                    speak('Should i remember this password?')
                    ans = voiceCommand()
                    if 'yes' in ans:
                        remember = open('password.txt', 'w')
                        remember.write(pas)
                        remember.close()
                        speak('Password saved')
                    else:
                        speak('Password is not saved')

                elif 'movie' in query:
                    movies_db = imdb.IMDB()
                    speak('Please tell me the movie name')
                    text = voiceCommand()
                    movies = movies_db.search_movie(text)
                    speak('Searching for' + text)
                    speak('i found these')
                    for movie in movies:
                        title = movie['title']
                        year = movie['year']
                        speak(f'{title}-{year}')
                        info = movie.getID()
                        movie_info = movies_db.get_movie(info)
                        rating = movie_info['rating']
                        cast = movie_info['cast']
                        actor = cast[0:5]
                        plot = movie_info.get(
                            'plot outline', 'plot summary not available')
                        speak(f'{title} was released in {year} had imdb rating of {rating}. It has cast of {actor}. The'
                              f'plot summary of movie is {plot}')
                        print(f'{title} was released in {year} had imdb rating of {rating}. It has cast of {actor}. The'
                              f'plot summary of movie is {plot}')

                elif 'calculate' in query:
                    app_id = 'QLH7WP-P6G7A2AKH9'
                    client = wolframalpha.ient(app_id)
                    ind = query.lower().split().index('calculate')
                    text = query.split()[inc + 1:]
                    result = client.query(" ".join(text))
                    try:
                        ans = next(result.result).text
                        speak('The answer is ' + ans)
                        print('The answer is ' + ans)
                    except StopIteration:
                        speak("i coundn't find that. PLease try again")

                elif 'what is' in query or 'who is' in query or 'which is' in query:
                    app_id = 'QLH7WP-P6G7A2AKH9'
                    client = wolframalpha.ient(app_id)
                    try:
                        ind = query.lower().index('what is') if 'what is' in query.lower() else\
                            query.lower().index('who is') if 'who is' in query.lower() else\
                            query.lower().index('which is') if 'which is' in query.lower() else None

                        if ind is not None:
                            text = query.split()[ind+2:]
                            result = client.query(" ".join(text))
                            ans = next(result.results).text
                            speak('The answer is' + ans)
                            print('The answer is' + ans)
                        else:
                            speak("i coundn't find that. PLease try again")
                    except StopIteration:
                        speak("I coudn't find that. Please try again later")

                elif 'offline' in query:
                    speak('Going Offline..')
                    speak('Thank you for using me')
                    quit()
