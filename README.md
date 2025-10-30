# Jarvis-AI voice assistant(python)
<br>
<br>
Overview:
<br>
Jarvis is a python based voice assistant which can perform tasks like fetching news , getting weather updates , playing music using the music library module , opening websites like google & amazon and lastly it has a locally installed AI model (ollama lama3:8b) support.
<br>
<br>
Trigger-word:
<br>
Jarvis uses **“Jarvis”** as a **wake word** —  

it stays passive until you say “Jarvis”, after which it actively listens for your next command.
<br>
<br>
✨ Features:
<br>
🧠 AI-Powered Responses-->

Integrated with the LLaMA model to generate smart and natural replies for general queries or conversations.

🗣️ Voice Recognition & Feedback-->

Understands spoken commands using SpeechRecognition, and replies with pyttsx3 (offline text-to-speech engine).

🌐 Smart Web Control-->

Opens popular websites like Google, YouTube, Amazon, and HiAnime using the Brave browser path set in .env.

🎵 Music Playback-->

Plays songs from a custom musiclibrary.py file — just say “Jarvis, play [song name]”.

📰 Live News Updates-->

Fetches and speaks top US news headlines using the News API, so you’re always up to date.

☁️ Real-Time Weather-->

Provides live weather and temperature updates through your custom Searchweather.py module.

⚙️ Modular & Extensible-->

Clean modular structure — easy to add new commands, APIs, or actions without touching core logic.

🔒 Secure Configuration-->

All sensitive data like API keys and browser paths are stored safely in a .env file (excluded from GitHub).



