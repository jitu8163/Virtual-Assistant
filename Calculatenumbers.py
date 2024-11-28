import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WolfRamAlpha(query):
    apikey = "QLH7WP-P6G7A2AKH9"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")
    Term = Term.replace("divide by", "/")
    Term = Term.replace("cross", "*")
    Term = Term.replace("percentile", "%")
    Term = Term.replace("into", "*")
    Term = Term.replace("x", "*")
    Term = Term.replace("point", ".")
    Term = Term.replace("power", "**")
    Term = Term.replace("raised to", "**")
    Term = Term.replace("modulus", "%")
    Term = Term.replace("remainder", "%")
    Term = Term.replace("over", "/")
    Term = Term.replace("divided by", "/")
    Term = Term.replace("add", "+")
    Term = Term.replace("subtract", "-")
    Term = Term.replace("times", "*")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")
