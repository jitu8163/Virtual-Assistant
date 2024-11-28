import time
import pyttsx3
import speech_recognition
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

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
        query = query.lower()  # Convert the query to lowercase
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def control_volume(query):
    """Control the system volume based on the command."""
    # Get default audio device (speakers)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume level
    current_volume = volume.GetMasterVolumeLevelScalar() * 100  # Get volume as percentage

    if 'increase volume' in query:
        speak("Increasing system volume.")
        time.sleep(1)
        new_volume = min(current_volume + 10, 100)  # Increase by 10%, max 100%
        volume.SetMasterVolumeLevelScalar(new_volume / 100, None)
        speak(f"Volume increased to {int(new_volume)} percent.")

    elif 'decrease volume' in query:
        speak("Decreasing system volume.")
        time.sleep(1)
        new_volume = max(current_volume - 10, 0)  # Decrease by 10%, min 0%
        volume.SetMasterVolumeLevelScalar(new_volume / 100, None)
        speak(f"Volume decreased to {int(new_volume)} percent.")

    elif 'set volume to' in query:
        # Example query: 'set volume to 50 percent'
        # Extract number
        volume_level = int(''.join([char for char in query if char.isdigit()]))
        speak(f"Setting volume to {volume_level} percent.")
        volume.SetMasterVolumeLevelScalar(volume_level / 100, None)
        speak(f"Volume set to {volume_level} percent.")


def control_brightness(query):

    if 'increase brightness' in query:
        speak("Increasing screen brightness.")
        time.sleep(1)
        current_brightness = sbc.get_brightness()[0]
        new_brightness = min(current_brightness + 10,
                             100)  # Increase by 10%, max 100%
        sbc.set_brightness(new_brightness)
        speak(f"Brightness increased to {new_brightness} percent.")

    elif 'decrease brightness' in query:
        speak("Decreasing screen brightness.")
        time.sleep(1)
        current_brightness = sbc.get_brightness()[0]
        new_brightness = max(current_brightness - 10,
                             0)  # Decrease by 10%, min 0%
        sbc.set_brightness(new_brightness)
        speak(f"Brightness decreased to {new_brightness} percent.")

    elif 'set brightness to' in query:

        # Extract the brightness level from the query
        bright_level = int(''.join([char for char in query if char.isdigit()]))
        speak(f"Setting brightness to {bright_level} percent.")
        sbc.set_brightness(bright_level)  # No need to divide by 100
        speak(f"Brightness set to {bright_level} percent.")


if __name__ == "__main__":
    while True:
        query = takeCommand()
        if 'increase volume' in query or 'volume up' in query:
            control_volume('increase volume')

        elif 'decrease volume' in query or 'volume down' in query:
            control_volume                                                              
            
            k('decrease volume')

        elif 'set volume to' in query:
            control_volume(query)
        elif 'increase brightness' in query or 'brightness up' in query:
            control_brightness('increase brightness')

        elif 'decrease brightness' in query or 'brightness down' in query:
            control_brightness('decrease brightness')

        elif 'set brightness to' in query:
            control_brightness(query)
