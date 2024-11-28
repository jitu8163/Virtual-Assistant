import pyttsx3
import speech_recognition
import time
import pyautogui
from datetime import datetime

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


def openWhatsApp():
    # This function opens WhatsApp from the system start menu using pyautogui
    pyautogui.press("super")  # Press the Windows key (super key)
    pyautogui.typewrite("Whatsapp")  # Type "WhatsApp"
    time.sleep(2)  # Wait for the search results to appear
    pyautogui.press("enter")  # Press Enter to open WhatsApp
    speak("Opening WhatsApp.")
    time.sleep(5)  # Wait for WhatsApp to fully load


def closeWhatsApp():
    # This function closes WhatsApp by simulating Alt + F4
    speak("Closing WhatsApp.")
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')


def sendMessage():
    contacts = {
        1: ("Ribhu", "Ribhu"),  # Use contact names as saved on WhatsApp
        2: ("Ruchika", "Ruchika"),
        3: ("Maa", "Maa"),
        4: ('Nikhil', 'Nikhil')
    }

    speak("Who do you want to message?")
    print('''1: Ribhu
             2: Ruchika
             3: Maa
             4: Nikhil''')

    try:
        choice = int(input("Enter the number corresponding to the contact: "))
        if choice in contacts:
            contact_name, whatsapp_contact = contacts[choice]
            speak(f"What's the message for {contact_name}?")
            message = takeCommand().lower()
            print(message)
            speak(message)
            # message = str(input("Enter the message: "))

            # Open WhatsApp using pyautogui
            openWhatsApp()

            # Simulate typing the contact name in the WhatsApp search bar
            pyautogui.hotkey('ctrl', 'f')  # Open search in WhatsApp
            pyautogui.typewrite(whatsapp_contact)
            time.sleep(1)

            # Press Enter to select the contact
            pyautogui.press('enter')
            time.sleep(2)  # Wait for the chat to open

            # Move focus from the search bar to the message input box by pressing 'tab' twice
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)

            # Type the message in the message input box
            pyautogui.typewrite(message)
            time.sleep(1)

            # Press Enter to send the message
            pyautogui.press('enter')
            speak("Message sent successfully.")

            # Close WhatsApp after sending the message
            closeWhatsApp()
        else:
            speak("Invalid choice.")
    except ValueError:
        speak("Invalid input. Please enter a number.")
    except Exception as e:
        speak("Failed to send the message.")
        print(f"Error: {e}")
