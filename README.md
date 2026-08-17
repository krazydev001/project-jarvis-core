# 🛡️ JARVIS 1.0

## AI Tactical HUD • Hardware Monitoring • Voice AI Assistant

<p align="center">

A futuristic AI desktop assistant built with Python and PyQt6 that combines real-time hardware telemetry, offline voice recognition, and AI-powered conversations.

</p>

---

## ✨ Features

# 📊 Real-Time Hardware Monitoring

Monitor your system performance with live animated telemetry widgets.

Features:

* CPU Usage Monitoring
* RAM Usage Monitoring
* GPU Activity Monitoring
* Network Upload Speed
* Network Download Speed
* Live Performance Graphs
* Real-Time System Statistics

---

# 🖥 Tactical HUD Interface

A futuristic dashboard inspired by sci-fi command interfaces.

Features:

* Full-screen HUD mode
* Custom PyQt6 widgets
* Animated interface elements
* Radar-style displays
* Live telemetry panels
* Dynamic status indicators
* Smooth UI animations
* Customizable themes

---

# 🔍 Hardware Information Panel

Hover over dashboard elements to view detailed hardware information.

Displays:

* CPU Model
* CPU Cores
* CPU Threads
* CPU Frequency
* Installed RAM
* System Information
* Hardware Profile

---

# 🎙 Voice AI Assistant

Voice-controlled AI interaction using:

* Vosk Offline Speech Recognition
* Groq API
* Llama 3.3 AI Model
* pyttsx3 Text-To-Speech

Features:

* Offline voice capture
* Speech-to-text conversion
* AI responses
* Voice reply generation
* Natural conversation

---

# 🤖 AI Intelligence

Powered by Groq Llama 3.3.

Features:

* Fast AI responses
* Question answering
* General conversations
* Smart assistant capabilities
* Context-based replies

---

# 🔊 Voice Output System

JARVIS can respond using generated speech.

Features:

* Text-To-Speech
* Voice playback
* Animated response display
* Real-time status updates

---

# ⚡ Performance Features

Designed for smooth continuous operation.

Includes:

* Multi-threaded processing
* Background workers
* Optimized telemetry updates
* Low resource usage
* Responsive UI

---

# 🛡 System Status Modes

JARVIS displays live system states:

```text
IDLE // SECURED STANDBY
```

```text
VOCAL CAPTURE ACTIVE
```

```text
NEURAL INTERPOLATION
```

```text
AUDIO SYNTH DISPATCH
```

---

# 📂 Project Structure

```text
jarvis-1.0/

│
├── core/
│   ├── brain.py
│   └── voice.py
│
├── ui/
│   └── Hud_widgets.py
│
├── model/
│   └── Vosk speech model
│
├── assets/
│
├── main.py
├── requirements.txt
├── api.env
└── README.md
```

---

# 🛠 Technologies Used

| Technology  | Purpose                    |
| ----------- | -------------------------- |
| Python      | Main language              |
| PyQt6       | User interface             |
| psutil      | Hardware monitoring        |
| numpy       | Data processing            |
| Vosk        | Offline speech recognition |
| sounddevice | Microphone input           |
| Groq API    | AI processing              |
| Llama 3.3   | Language model             |
| pyttsx3     | Text-to-speech             |

---

# 🚀 Future Roadmap

Planned features:

* Wake word detection
* Weather integration
* Application launcher
* Local LLM support
* Plugin system
* Smart automation
* Mobile companion app

---

# 👨‍💻 Author

**krazydev001**

Building AI-powered desktop applications, automation tools, and futuristic Python projects.

---

# 🎙️ Vosk Setup

JARVIS requires a Vosk speech recognition model for voice commands.

JARVIS is configured to load the speech recognition model from:

```text
model
```

You can use different compatible Vosk models by replacing the contents of this folder. **You do not need to change the JARVIS source code when switching between compatible models.**

---

# 1. Download a Vosk Model

Vosk provides multiple speech recognition models with different sizes and languages.

Official Vosk Models:

```text
https://alphacephei.com/vosk/models
```

For example, the recommended English model is:

```text
vosk-model-small-en-us-0.15
```

Direct Download:

```text
https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
```

You can also choose another compatible Vosk model from the official model list.

---

# 2. Extract the ZIP File

After downloading the model, extract the ZIP file.

For example:

```text
vosk-model-small-en-us-0.15.zip
```

After extraction you will get:

```text
vosk-model-small-en-us-0.15
```

The exact folder name depends on the model you downloaded.

---

# 3. Rename the Model Folder

Rename the extracted model folder to:

```text
model
```

For example:

```text
vosk-model-small-en-us-0.15
```

becomes:

```text
model
```

The folder name must be exactly:

```text
model
```

---

# 4. Move the Model Folder

Place the `model` folder directly inside your JARVIS project directory.

Your structure should look like:

```text
jarvis-1.0/

│
├── model/
│   ├── am/
│   ├── conf/
│   ├── graph/
│   ├── ivector/
│   └── ...
│
├── core/
│   ├── brain.py
│   └── voice.py
│
├── ui/
│   └── Hud_widgets.py
│
├── assets/
│
├── main.py
├── requirements.txt
└── api.env
```

The important part is:

```text
jarvis-1.0/
└── model/
```

---

# 5. Model Folder Must Not Be Nested

Do **not** put the model inside another folder.

Correct:

```text
jarvis-1.0/
└── model/
    ├── am/
    ├── conf/
    ├── graph/
    └── ivector/
```

Incorrect:

```text
jarvis-1.0/
└── model/
    └── vosk-model-small-en-us-0.15/
        ├── am/
        ├── conf/
        ├── graph/
        └── ivector/
```

The Vosk model files must be directly inside the `model` folder.

---

# 6. Changing Vosk Models

You can switch to another compatible Vosk model at any time.

Simply:

1. Download another Vosk model.
2. Extract it.
3. Rename its main folder to `model`.
4. Replace the existing `model` folder.
5. Start JARVIS.

For example:

```text
Old model:

vosk-model-small-en-us-0.15
        ↓
      model
```

You can later replace it with another compatible model:

```text
Another Vosk model
        ↓
      model
```

JARVIS will continue loading:

```text
model
```

No changes to `core/voice.py` are required.

---

# 7. Install Vosk

Activate your virtual environment first.

Then run:

```bash
pip install vosk
```

---

# 8. Install Audio Support

Install microphone support:

```bash
pip install sounddevice
```

---

# 9. Verify Vosk Installation

Run:

```bash
pip show vosk
```

You should see:

```text
Name: vosk
Version: x.x.x
```

---

# 10. Test JARVIS

Run:

```bash
python main.py
```

If the model is installed correctly, JARVIS will load the model from:

```text
model/
```

and start normally.

The `model` folder must remain in the same directory as:

```text
main.py
```

---

# Troubleshooting

## Model Not Found

Make sure your folder is:

```text
jarvis-1.0/model
```

Correct:

```text
jarvis-1.0/
└── model/
    ├── am/
    ├── conf/
    ├── graph/
    └── ivector/
```

Incorrect:

```text
jarvis-1.0/
└── vosk-model-small-en-us-0.15/
```

Rename the extracted model folder to:

```text
model
```

---

## Missing Model Files

Different Vosk models can contain different files and folders.

Do not manually rename or modify the internal model files.

Instead, download the model again from the official Vosk model page if the extraction appears incomplete.

Official Vosk Models:

```text
https://alphacephei.com/vosk/models
```

---

## Model Loading Error

If JARVIS shows:

```text
Exception: Failed to create a model
```

check:

* `model` exists in the project directory
* The model is extracted correctly
* The model is not nested inside another folder
* You downloaded a compatible Vosk model
* The model files were not modified or deleted

The expected location is:

```text
jarvis-1.0/model
```

---

## Microphone Error

Make sure:

* Microphone is connected
* Microphone permission is enabled
* Default recording device is selected
* `sounddevice` is installed

Install again if necessary:

```bash
pip install sounddevice
```

---

## Vosk Setup Complete

JARVIS can use different compatible Vosk speech recognition models by replacing the `model` folder.

No source-code changes are required when switching between compatible models.

---

# 🐍 Python Setup & Installation

Follow these steps to install and run JARVIS 1.0.

---

# 1. Requirements

Before installing JARVIS, make sure you have:

* Python 3.12+
* Git
* VS Code (Recommended)
* Microphone
* Internet connection for Groq AI responses

---

# 2. Install Python

Download Python:

```text
https://www.python.org/downloads/
```

During installation enable:

```text
Add Python to PATH
```

Verify installation:

```bash
python --version
```

Example:

```text
Python 3.12.x
```

---

# 3. Clone Repository

Clone the project:

```bash
git clone <your-repository-url>
```

Open the project folder:

```bash
cd jarvis-1.0
```

---

# 4. Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

---

# 5. Activate Virtual Environment

## Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

## Linux / macOS

```bash
source .venv/bin/activate
```

After activation:

```text
(.venv)
```

will appear in your terminal.

---

# 6. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

Main dependencies:

```text
PyQt6
psutil
numpy
sounddevice
vosk
pyttsx3
groq
python-dotenv
```

---

# 7. Configure Groq API

JARVIS uses the Groq API for AI responses.

Create a file named:

```text
api.env
```

inside the project folder.

Add your API key:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
```

---

# 8. Get a Groq API Key

Create an account and generate an API key:

```text
https://console.groq.com
```

Add the API key to:

```text
api.env
```

---

# 9. Protect Your API Key

Never upload your API key to GitHub.

Add this to `.gitignore`:

```gitignore
api.env
```

You should also avoid posting your API key publicly.

If an API key is accidentally exposed, revoke it and generate a new one.

---

# 10. Final Project Structure

Before running JARVIS, your project should look like:

```text
jarvis-1.0/

│
├── model/
│   ├── am/
│   ├── conf/
│   ├── graph/
│   └── ivector/
│
├── core/
│   ├── brain.py
│   └── voice.py
│
├── ui/
│   └── Hud_widgets.py
│
├── assets/
│
├── .venv/
│
├── api.env
├── requirements.txt
├── main.py
├── .gitignore
└── README.md
```

---

# 11. Run JARVIS

Activate your environment:

```bash
.venv\Scripts\activate
```

Start the application:

```bash
python main.py
```

---

# 12. First Startup

JARVIS will initialize:

```text
Loading Interface...

Starting Telemetry...

Loading Voice Engine...

Loading Vosk Model...

Connecting AI Engine...

System Ready
```

---

# 13. Exit Application

Press:

```text
ESC
```

to safely close JARVIS.

---

# Troubleshooting

## Python Not Found

Install Python again and make sure:

```text
Add Python to PATH
```

is enabled.

Then restart your terminal and run:

```bash
python --version
```

---

## Missing Packages

Run:

```bash
pip install -r requirements.txt
```

---

## Groq Error

Check that:

```text
api.env
```

contains:

```env
GROQ_API_KEY=YOUR_KEY
```

Make sure you have not accidentally added spaces or quotes around the key.

---

## Voice Not Working

Check:

* Vosk model exists
* `model` folder is in the project root
* Microphone permissions are enabled
* Correct microphone is selected
* `sounddevice` is installed
* Vosk is installed

Install again if necessary:

```bash
pip install sounddevice vosk
```

---

## Application Does Not Start

Run:

```bash
python main.py
```

and check the terminal error message.

The terminal output usually identifies the component causing the problem.

---

# ✅ Installation Complete

JARVIS 1.0 is now ready.

Features enabled:

✅ Tactical HUD Dashboard
✅ Hardware Monitoring
✅ Offline Voice Recognition
✅ Groq AI Assistant
✅ Text-To-Speech Response
