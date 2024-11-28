# from INTRO import start_media
from spotify import play_song, pause_song, resume_song, next_song, previous_song
import pyttsx3
import speech_recognition
import datetime
import random
import webbrowser
from pygame import mixer
from plyer import notification
import speedtest
import requests
from bs4 import BeautifulSoup
import pyautogui
import os
import pyjokes
import keyboard
import time
import ctypes
import winshell
import subprocess
from playlist_links import playlist_dict
from control import control_brightness, control_volume
from spotify import play_song, pause_song, resume_song, next_song, previous_song

# start_media()

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
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        speak("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        # play_gif

        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try Again")


def scroll_window(scroll_amount):

    pyautogui.scroll(scroll_amount)


def switch_window():
    """
    Switches to the next window (like ALT+TAB).
    """
    pyautogui.hotkey('alt', 'tab')
    speak("Switched window.")


def minimize_window():
    """
    Minimizes the current window.
    """
    pyautogui.hotkey('win', 'down')
    speak("Window minimized.")


def maximize_window():
    """
    Maximizes the current window.
    """
    pyautogui.hotkey('win', 'up')
    speak("Window maximized.")


def close_window():
    """
    Closes the current window.
    """
    pyautogui.hotkey('alt', 'f4')
    speak("Window closed.")


def open_application(app_name):

    speak(f"Opening {app_name}")
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write(app_name)
    pyautogui.press("enter")


def navigate_start_menu():

    pyautogui.press("win")
    speak("Opened start menu.")


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:

        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you ?")

                elif "i am fine" in query:
                    speak("that's great, sir")

                elif 'fine' in query or "good" in query:
                    speak("It's good to know that your fine")

                elif "how are you" in query:
                    speak("Perfect, sir")

                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif "who made you" in query or "who created you" in query:
                    speak("I have been created by Jitendra And Ribhu.")

                elif "who i am" in query:
                    speak("If you talk then definitely your human.")

                elif 'joke' in query:
                    speak(pyjokes.get_joke())

                elif "why you came to world" in query:
                    speak("Thanks to Jeetu and Ribhu. further It's a secret")

                elif 'is love' in query:
                    speak("It is 7th sense that destroy all other senses")

                elif "who are you" in query:
                    speak("I am your virtual assistant created by Jitendra And Ribhu")

                elif 'reason for you' in query:
                    speak("I was created as a Minor project by Jitu and Ribhu ")

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    speak('Opening YouTube')
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in Jaipur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    speak('For which city you want to check the weather')
                    city = takeCommand()
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

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)

                elif "switch window" in query:
                    switch_window()

                elif "minimise window" in query:
                    minimize_window()

                elif "maximize window" in query:
                    maximize_window()

                elif "close window" in query:
                    close_window()

                elif "open notepad" in query:
                    open_application("notepad")

                elif "start menu" in query:
                    navigate_start_menu()

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "fullscreen" in query or "full screen" in query:
                    pyautogui.press("f")
                    speak("fullscreen")

                elif "pause" in query or "pose" in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif 'increase volume' in query or 'volume up' in query:
                    control_volume('increase volume')

                elif 'decrease volume' in query or 'volume down' in query:
                    control_volume('decrease volume')

                elif 'set volume to' in query:
                    control_volume(query)

                elif 'increase brightness' in query or 'brightness up' in query:
                    control_brightness('increase brightness')

                elif 'decrease brightness' in query or 'brightness down' in query:
                    control_brightness('decrease brightness')

                elif 'set brightness to' in query:
                    control_brightness(query)

                elif 'turn on Keyboard light' in query or 'lights on' in query:
                    speak("turning on Keyboard light.")
                    time.sleep(1)
                    pyautogui.hotkey('alt', 'f10')
                    speak("Keyboard light turned on.")

                elif 'turn of Keyboard light' in query or 'lights of' in query or 'turn off Keyboard light' in query or 'lights off' in query:
                    speak("turning off Keyboard light.")
                    time.sleep(1)
                    pyautogui.hotkey('alt', 'f10')
                    speak("Keyboard light turned off.")

                elif "spotify" in query:
                    song_name = query.replace("play song", "").strip()
                    play_song(song_name)

                elif "pause song" in query:
                    pause_song()

                elif "resume song" in query:
                    resume_song()

                elif "next song" in query:
                    next_song()

                elif "previous song" in query:
                    previous_song()

                elif "scroll up" in query:
                    scroll_window(500)  # Scrolls up
                    # speak("Scrolled up.")

                elif "scroll down" in query:
                    scroll_window(-500)  # Scrolls down
                    # speak("Scrolled down.")

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to remember that" + remember.read())

                elif "write a note" in query:
                    speak("What should i write, sir")
                    note = takeCommand()
                    file = open('jarvis.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = takeCommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("% H:% M:% S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)

                elif "show note" in query or "show notes" in query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    print(file.read())
                    speak(file.read(6))

                elif "tired" in query or "song" in query or "music" in query:
                    speak("Playing a song from your favourite Playlist, sir")
                    # Get all keys (numbers) from the dictionary
                    playlist_keys = list(playlist_dict.keys())
                    random_key = random.choice(
                        playlist_keys)  # Choose a random key
                    # Get the playlist link associated with the random key
                    selected_link = playlist_dict[random_key]
                    webbrowser.open(selected_link)
                    time.sleep(10)  # Wait for the browser to open the link
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    pyautogui.press('tab')  # Navigate to the video player
                    # pyautogui.press('tab')  # Navigate to the video player
                    # pyautogui.press('tab')  # Navigate to the video player
                    # pyautogui.press('tab')  # Navigate to the video player

                    pyautogui.press('enter')
                    pyautogui.press('enter')  # Play the video
                    # Play the video

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif 'send a mail' in query:
                    from sendEmail import Email
                    Email()

                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )

                elif "open" in query:  # EASY METHOD
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Best server: ", wifi.get_best_server())
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ", download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                elif "ipl score" in query:
                    from fetch_ipl_score import fetch_ipl_score
                    fetch_ipl_score()

                elif "game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                    try:
                        # Take a screenshot
                        screenshot = pyautogui.screenshot()

                        # Save the screenshot
                        screenshot.save("ss.jpg")

                        print("Screenshot saved as ss.jpg")
                    except Exception as e:
                        print(f"Error taking screenshot: {e}")

                elif "click my photo" in query or "take my photo" in query or "capture image" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.sleep(3)
                    pyautogui.press("enter")
                    pyautogui.press("enter")
                    speak('I took your 2 pictures.')
                    pyautogui.sleep(5)
                    pyautogui.hotkey('alt', 'f4')

                elif "focus mode" in query:
                    a = int(input(
                        "Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a == 1):
                        speak("Entering the focus mode....")
                        os.startfile(
                            r"C:\Users\Dell\OneDrive\Desktop\EDU Projects\Jarvis\FocusMode.py")

                    else:
                        pass

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl(query)

                elif "restart" in query:
                    subprocess.call(["shutdown", "/r"])

                elif "hibernate" in query or "sleep" in query:
                    speak("Hibernating")
                    subprocess.call("shutdown / h")

                elif "log off" in query or "sign out" in query:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    subprocess.call(["shutdown", "/l"])

                elif 'lock window' in query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input(
                        "Do you wish to shutdown your computer? (y/n)")
                    if shutdown == "y":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "n":
                        break

                elif 'empty recycle bin' in query:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    speak("Recycle Bin Recycled")

                elif "don't listen" in query or "stop listening" in query:
                    speak(
                        "For how much time do you want to stop Jarvis from listening to commands? Please specify seconds or minutes.")

                    time_input = takeCommand()  # Take the input from user (in seconds or minutes)

                    # Splitting the input based on user mentioning "minutes" or "seconds"
                    if "minute" in time_input:
                        a = int(time_input.replace("minutes", "").strip()) * \
                            60  # Convert minutes to seconds
                    elif "second" in time_input:
                        # Directly use seconds
                        a = int(time_input.replace("seconds", "").strip())
                    else:
                        speak(
                            "Sorry, I didn't get that. Please specify the time in either seconds or minutes.")
                        a = 0  # Set a default in case input is unclear

                    if a > 0:
                        speak(f"Stopping listening for {a} seconds.")
                        time.sleep(a)  # Stop listening for 'a' seconds
                        speak("Resuming now.")
                    else:
                        speak("Invalid time specified.")

                elif "go to sleep" in query:
                    speak("Going to sleep,sir")
                    speak('Feel free to wake me up.')
                    exit()

                elif 'exit' in query:
                    speak('Going Offline..')
                    speak("Thanks for giving me your time")
                    exit()

                elif 'offline' in query:
                    speak('Going Offline..')
                    speak('Thank you for using me')
                    quit()
