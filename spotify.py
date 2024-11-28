import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    """Function to speak audio using pyttsx3."""
    engine.say(audio)
    engine.runAndWait()


# Spotify Authentication details
CLIENT_ID = '654459b4432948aab909f7675c8f81a4'
CLIENT_SECRET = '6d4032c6848f46ad92eb1d4cce7f04be'
REDIRECT_URI = 'http://localhost:8888/callback'

# Initialize Spotify Client
scope = "user-read-playback-state user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))


def play_song(song_name):
    """Search for a song and play it on Spotify."""
    results = sp.search(q=song_name, limit=1)
    if results['tracks']['items']:
        song_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[song_uri])
        speak(f"Playing {song_name} on Spotify")
    else:
        speak(f"Could not find {song_name} on Spotify")


def pause_song():
    """Pause the current playing song on Spotify."""
    sp.pause_playback()
    speak("Paused the song on Spotify")


def resume_song():
    """Resume the paused song on Spotify."""
    sp.start_playback()
    speak("Resumed the song on Spotify")


def next_song():
    """Skip to the next song on Spotify."""
    sp.next_track()
    speak("Skipped to the next song on Spotify")


def previous_song():
    """Go back to the previous song on Spotify."""
    sp.previous_track()
    speak("Playing the previous song on Spotify")
