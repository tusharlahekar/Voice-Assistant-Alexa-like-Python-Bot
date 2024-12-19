# Voice-Assistant: Alexa-like Python Bot

This project is a simple voice assistant developed in Python. Inspired by Alexa, it can listen to voice commands, respond intelligently, and perform tasks such as playing songs on YouTube, telling the time, giving Wikipedia summaries, cracking jokes, and more.

---

## Features
- **Play Music**: Plays songs directly from YouTube based on your command.
- **Time Announcement**: Tells you the current time.
- **Wikipedia Lookup**: Provides a brief summary of the requested topic.
- **Joke Telling**: Shares a random joke to lighten your mood.
- **Custom Responses**: Engages in light-hearted conversations.

---

## Technologies Used
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)**: For recognizing and processing voice commands.
- **[pyttsx3](https://pypi.org/project/pyttsx3/)**: For text-to-speech conversion.
- **[pywhatkit](https://pypi.org/project/pywhatkit/)**: For playing YouTube videos.
- **[wikipedia](https://pypi.org/project/wikipedia/)**: For fetching Wikipedia summaries.
- **[pyjokes](https://pypi.org/project/pyjokes/)**: For generating random jokes.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant

Install the required dependencies:

bash
Copy code
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
Run the script:

bash
Copy code
python voice_assistant.py
Usage
Start the program, and the assistant will begin listening.
Say commands like:
"Alexa, play [song name]"
"Alexa, what time is it?"
"Alexa, who is [person's name]?"
"Alexa, tell me a joke."
Enjoy interacting with your personal voice assistant!
Example Commands
"Alexa, play Shape of You"
"Alexa, what is the time?"
"Alexa, who is Albert Einstein?"
"Alexa, are you single?"
Customization
Feel free to enhance the assistant by adding more features. Some ideas include:

Weather forecasts
Alarm and reminders
Smart home integration
Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.
