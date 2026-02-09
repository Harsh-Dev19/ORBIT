import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random

# ---------- SPEECH ----------


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ---------- LISTEN ----------
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

# ---------- MUSIC PATH (CHANGE THIS ONLY) ----------
music_folder = r"C:\Users\Admin\Downloads"

speak("ORBIT is online. You can give commands.")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        responded = False

        # BASIC COMMANDS
        if "hello" in command:
            speak("Hello! How can I help you?")
            responded = True

        if "time" in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}")
            responded = True

        if "date" in command:
            date_now = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date_now}")
            responded = True

        # WEBSITE COMMANDS
        if "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            responded = True

        if "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            responded = True

        # MUSIC COMMAND
        if "play music" in command:
            songs = [f for f in os.listdir(music_folder) if f.lower().endswith(".mp3")]
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_folder, song))
                speak("Playing music")
            else:
                speak("No music files found")
            responded = True

        # STOP
        if "stop" in command:
            speak("Goodbye. ORBIT shutting down.")
            break

        if not responded:
            speak("Sorry, I don't understand that command.")

    except:
        print("Could not understand audio")
