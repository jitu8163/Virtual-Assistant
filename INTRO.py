from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time
import pygame  # pip install pygame
from pygame import mixer
import cv2
import threading
mixer.init()

root = Tk()
root.geometry("500x500")

# Function to play starting video


# def play_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         cv2.imshow('Startup Video', frame)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# Function to play starting sound


def play_sound(sound_path):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for the sound to finish playing
        pygame.time.Clock().tick(10)


# def play_gif_in_loop(gif_path):
#     lbl = Label(root)  # Create a Label widget to display GIF
#     lbl.pack()

    # gif = Image.open(gif_path)  # Open the GIF file

    # Infinite loop to keep playing the GIF
    # while True:
    #     for img in ImageSequence.Iterator(gif):
    #         # Resize the GIF (adjust size as needed)
    #         img = img.resize((250, 250))
    #         img = ImageTk.PhotoImage(img)
    #         lbl.config(image=img)
    #         root.update()
    #         # Control the speed of GIF playback (100 ms delay per frame)
    #         root.after(50)

# Function to start video and sound, then play GIF in loop


def start_media():
    # Start video and sound in parallel threads
    # video_thread = threading.Thread(target=play_video, args=(
    #     r'C:\Users\Dell\OneDrive\Desktop\EDU Projects\Jarvis\2019-07-10+14-48-21.mp4',))
    sound_thread = threading.Thread(target=play_sound, args=(
        r'C:\Users\Dell\OneDrive\Desktop\EDU Projects\Jarvis\2019-07-1014-48-21.mp3',))

    # video_thread.start()
    sound_thread.start()

    # Wait for video and sound to complete
    # video_thread.join()
    sound_thread.join()

    # Once video and sound are done, play GIF in infinite loop
    # play_gif_in_loop(
    #     r'C:\Users\Dell\OneDrive\Desktop\EDU Projects\Jarvis\giphy.gif')


# Start the media playback process
start_media()

# Tkinter main loop
root.mainloop()
