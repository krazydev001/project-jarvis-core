# 🛡️ JARVIS 3.0
## AI Tactical HUD • Hardware Monitoring • Voice AI Assistant

<p align="center">

A futuristic AI desktop assistant built with Python and PyQt6 that combines real-time hardware telemetry, offline voice recognition, and AI-powered conversations.

</p>

---

## ✨ Features

# 📊 Real-Time Hardware Monitoring

Monitor your system performance with live animated telemetry widgets.

Features:

- CPU Usage Monitoring
- RAM Usage Monitoring
- GPU Activity Monitoring
- Network Upload Speed
- Network Download Speed
- Live Performance Graphs
- Real-Time System Statistics

---

# 🖥 Tactical HUD Interface

A futuristic dashboard inspired by sci-fi command interfaces.

Features:

- Full-screen HUD mode
- Custom PyQt6 widgets
- Animated interface elements
- Radar-style displays
- Live telemetry panels
- Dynamic status indicators
- Smooth UI animations
- Customizable themes

---

# 🔍 Hardware Information Panel

Hover over dashboard elements to view detailed hardware information.

Displays:

- CPU Model
- CPU Cores
- CPU Threads
- CPU Frequency
- Installed RAM
- System Information
- Hardware Profile

---

# 🎙 Voice AI Assistant

Voice-controlled AI interaction using:

- Vosk Offline Speech Recognition
- Groq API
- Llama 3.3 AI Model
- pyttsx3 Text-To-Speech

Features:

- Offline voice capture
- Speech-to-text conversion
- AI responses
- Voice reply generation
- Natural conversation

---

# 🤖 AI Intelligence

Powered by Groq Llama 3.3.

Features:

- Fast AI responses
- Question answering
- General conversations
- Smart assistant capabilities
- Context-based replies

---

# 🔊 Voice Output System

JARVIS can respond using generated speech.

Features:

- Text-to-Speech
- Voice playback
- Animated response display
- Real-time status updates

---

# ⚡ Performance Features

Designed for smooth continuous operation.

Includes:

- Multi-threaded processing
- Background workers
- Optimized telemetry updates
- Low resource usage
- Responsive UI

---

# 🛡 System Status Modes

JARVIS displays live system states:

```
IDLE // SECURED STANDBY
```

```
VOCAL CAPTURE ACTIVE
```

```
NEURAL INTERPOLATION
```

```
AUDIO SYNTH DISPATCH
```

---

# 📂 Project Structure

```
jarvis-3.0/

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
│
├── requirements.txt
│
├── api.env
│
└── README.md
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|-|-|
| Python | Main language |
| PyQt6 | User interface |
| psutil | Hardware monitoring |
| numpy | Data processing |
| Vosk | Offline speech recognition |
| sounddevice | Microphone input |
| Groq API | AI processing |
| Llama 3.3 | Language model |
| pyttsx3 | Text-to-speech |

---

# 🚀 Future Roadmap

Planned features:

- Wake word detection
- Weather integration
- Application launcher
- Local LLM support
- Plugin system
- Smart automation
- Mobile companion app

---

# 👨‍💻 Author

**krazydev001**

Building AI-powered desktop applications, automation tools, and futuristic Python projects.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🎙️ Vosk Setup

JARVIS requires the Vosk speech recognition model for voice commands.

Follow the steps below to install it.

---

# 1. Download Vosk Model

Download the recommended English model:

**Model:**

```
vosk-model-small-en-us-0.15
```

Official Vosk Models:

```
https://alphacephei.com/vosk/models
```

Direct Download:

```
https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
```

---

# 2. Extract the ZIP File

After downloading:

```
vosk-model-small-en-us-0.15.zip
```

Extract it.

You will get:

```
vosk-model-small-en-us-0.15
```

---

# 3. Rename the Folder

Rename:

```
vosk-model-small-en-us-0.15
```

to:

```
model
```

The folder name must be exactly:

```
model
```

---

# 4. Move Model Folder

Place the `model` folder inside your JARVIS project directory.

Your structure should look like:

```
jarvis-3.0/

│
├── model/
│   ├── am/
│   ├── conf/
│   ├── graph/
│   ├── ivector/
│   └── README
│
├── core/
│
├── ui/
│
├── main.py
│
├── requirements.txt
│
└── api.env
```

---

# 5. Install Vosk Package

Activate your virtual environment first.

Then run:

```bash
pip install vosk
```

---

# 6. Install Audio Support

Install microphone support:

```bash
pip install sounddevice
```

---

# 7. Verify Installation

Check Vosk installation:

```bash
pip show vosk
```

You should see:

```
Name: vosk
Version: x.x.x
```

---

# 8. Test JARVIS

Run:

```bash
python main.py
```

If the model is installed correctly, JARVIS will start normally.

The `model` folder must remain in the same directory as:

```
main.py
```

---

# Troubleshooting

## Model Not Found

Check that your folder is:

Correct:

```
jarvis-3.0/model
```

Incorrect:

```
jarvis-3.0/vosk-model-small-en-us-0.15
```

Rename it to:

```
model
```

---

## Missing Model Files

The model folder should contain:

```
model/

├── am
├── conf
├── graph
└── ivector
```

If these are missing, download and extract the model again.

---

## Microphone Error

Make sure:

- Microphone is connected
- Microphone permission is enabled
- Default recording device is selected

---

✅ Vosk setup complete.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🐍 Python Setup & Installation

Follow these steps to install and run JARVIS 3.0.

---

# 1. Requirements

Before installing JARVIS, make sure you have:

- Python 3.12+
- Git
- VS Code (Recommended)
- Microphone
- Internet connection (Required for Groq AI responses)

---

# 2. Install Python

Download Python:

```
https://www.python.org/downloads/
```

During installation enable:

```
☑ Add Python to PATH
```

Verify installation:

```bash
python --version
```

Example:

```
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
cd jarvis-3.0
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

```
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

```
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

JARVIS uses Groq API for AI responses.

Create a file:

```
api.env
```

inside the project folder.

---

Add your API key:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
```

---

# 8. Get Groq API Key

Create an account:

```
https://console.groq.com
```

Generate an API key and add it to:

```
api.env
```

---

# 9. Protect API Key

Never upload your API key.

Add this to `.gitignore`:

```gitignore
api.env
```

---

# 10. Final Project Structure

Before running, your folder should look like:

```
jarvis-3.0/

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
│
├── requirements.txt
│
├── main.py
│
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

```
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

```
ESC
```

to safely close JARVIS.

---

# Troubleshooting

## Python Not Found

Install Python again and enable:

```
Add Python to PATH
```

---

## Missing Packages

Run:

```bash
pip install -r requirements.txt
```

---

## Groq Error

Check:

```
api.env
```

contains:

```env
GROQ_API_KEY=YOUR_KEY
```

---

## Voice Not Working

Check:

- Vosk model exists
- Microphone permissions enabled
- sounddevice installed

Install again:

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

---

# ✅ Installation Complete

JARVIS 3.0 is now ready.

Features enabled:

✅ Tactical HUD Dashboard  
✅ Hardware Monitoring  
✅ Offline Voice Recognition  
✅ Groq AI Assistant  
✅ Text-To-Speech Response  
