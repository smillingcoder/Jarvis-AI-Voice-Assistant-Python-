# ⚙️ Jarvis Installation Guide

---

## 🧠 Prerequisites

Before starting, make sure you have:

- 🐍 **Python 3.8+** → [Download Python](https://www.python.org/downloads/).
- 🌐 **Internet connection** (for APIs).
- 🦙 **Ollama installed** → [Download Ollama](https://ollama.com/download).
- 🧩 Basic understanding of Python.

---

## Step1️⃣ Clone the Repository

_Run these in your vs code terminal_

git clone https://github.com/smillingcoder/Jarvis-py.git

cd Jarvis 

(press tab after typing jar it will automatically enter jarvis)

---

## Step2️⃣ (Optional) Create a Virtual Environment🧱

_Run this in your vs code terminal_

python -m venv venv

-Then activate it , if its activated you will see (.venv) appearing in your terminal.

---

## Step3️⃣ Install Dependencies📦

_Run this in your vs code terminal_

pip install -r requirements.txt

-Make sure requirements.txt includes:

speechrecognition

pyttsx3

requests

python-dotenv

(this will install all necessary python packages required to run jarvis)

---

## Step4️⃣ Configure the .env File🔑

-Create a .env file in your project root and add your keys and paths as shown in .env.example👇

news_api_key=your_news_api_key_here

weather_api_key=your_weather_api_key_here

BRAVE_PATH=C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe

💡Resources:

📰 Get a free News API key from https://newsapi.org

☁️ Get a free Weather API key from https://home.openweathermap.org/

🦁 Update the Brave path if installed elsewhere or change it if you're using a different browser.

---

## Step5️⃣ Setup Ollama + LLaMA 3 Model🦙

-Jarvis uses LLaMA 3 via Ollama for intelligent chat replies.

After installing Ollama, run:

_Run this in your system cmd_

ollama pull llama3

-Confirm it’s installed:

_Run this in your system cmd_

ollama list

(you will see llama3 there if its installed correctly)

---

## Step6️⃣ Run Jarvis 🚀

-Start your assistant in vs code terminal

-You’ll see:

Initializing jarvis....

Listening...

-Then say:

🎤 "Jarvis" → it will reply "Yes?"

Now give your command, like:

“Open YouTube”

“Play skyfall”

“What’s the weather?”

“Tell me the news”

“Who are you?”

---

## Step7️⃣ (Optional) Customize Jarvis 

-Change default city for weather in:

speak(temperature("your_city"))

-Add your own songs inside musiclibrary.py

-Change the wake word (“Jarvis”) to whatever you like

---

## Completion 🎉

---

## 👨‍💻 Author

_Sohum Tiwari_  

_B.Tech CSE (AIML) Undergrad🎓_

---

_**If you like this project, don't forget to ⭐ on the repo!**_

