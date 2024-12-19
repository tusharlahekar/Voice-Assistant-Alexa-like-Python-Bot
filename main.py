import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Configure voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index for male/female voice

def talk(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to the user's command and return it as text."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Command received: {command}")
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""

def run_alexa():
    """Main function to execute Alexa-like commands."""
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Current time is {time}")
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, sentences=1)
        talk(info)
    elif 'date' in command:
        talk("Sorry, I have a headache.")
    elif 'are you single' in command:
        talk("I am in a relationship with Wi-Fi.")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("I didn't understand. Please repeat.")

# Run the voice assistant
while True:
    run_alexa()
