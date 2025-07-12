import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit

r = sr.Recognizer()

engine = pyttsx3.init()

def processCommand(command):
    command = command.lower().strip()

    # Handle play command
    if command.startswith("play"):
        song = command.replace("play", "", 1).strip()
        if song:
            speak(f"Playing {song} on YouTube...")
            pywhatkit.playonyt(song)
        else:
            speak("Please mention the song name after 'play'.")

    # Handle open command
    elif command.startswith("open"):
        site = command.replace("open", "", 1).strip()

        if site:
            site_map = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "gmail": "https://mail.google.com",
                "github": "https://github.com",
                "stack overflow": "https://stackoverflow.com",
                "google docs": "https://docs.google.com",
                "google drive": "https://drive.google.com",
            }

            url = site_map.get(site, f"https://www.{site.replace(' ', '')}.com")
            speak(f"Opening {site}")
            webbrowser.open(url)
        else:
            speak("Please say the website name after 'open'.")

    else:
        speak("Sorry, I didn't understand the command. Try saying 'play song' or 'open website'.")

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Groot...")
    while True:
        print("Recognizing...")

        with sr.Microphone() as source:
            print("Listening...")

            try:
                # Wait max 5 seconds to start speaking, max 5 sec of speech
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected.")
                continue

        try:
            word = r.recognize_google(audio)
            print(" ", word)

            if word.lower() == "hello":
                speak("I'm Groot")
                # You can now add more logic here to listen for the next word
                with sr.Microphone() as source:
                    print("Groot Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
        except sr.RequestError as e:
            print(f"Google Recognition error: {e}")
