# core/voice.py
import os
import json
import queue
import time
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from PyQt6.QtCore import QThread, pyqtSignal

class VoiceWorker(QThread):
    state_changed = pyqtSignal(str)     # 'listening', 'thinking', 'speaking', 'idle'
    text_recognized = pyqtSignal(str)   

    def __init__(self, model_path="models/vosk-model-small-en-us-0.15"):
        super().__init__()
        absolute_model_path = os.path.abspath(model_path)
        
        if not os.path.exists(os.path.join(absolute_model_path, "am")):
            nested_path = os.path.join(absolute_model_path, "vosk-model-small-en-us-0.15")
            if os.path.exists(os.path.join(nested_path, "am")):
                absolute_model_path = nested_path

        self.model = Model(absolute_model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.audio_queue = queue.Queue()
        self.running = True
        
        # Listening gate parameters
        self.active_listening = False
        self.activation_timestamp = 0.0
        self.listening_timeout = 5.0  # Seconds allowed to input command after saying Jarvis

    def audio_callback(self, indata, frames, time_info, status):
        self.audio_queue.put(bytes(indata))

    def run(self):
        with sd.RawInputStream(samplerate=16000, blocksize=4000, dtype='int16',
                               channels=1, callback=self.audio_callback):
            while self.running:
                data = self.audio_queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "").lower().strip()
                    
                    if not text:
                        continue
                    
                    current_time = time.time()
                    
                    # Check if the listening window expired naturally
                    if self.active_listening and (current_time - self.activation_timestamp > self.listening_timeout):
                        self.active_listening = False
                        self.state_changed.emit("idle")
                        print("🔒 System: Wake window closed. Standing by...")

                    # Look for Activation Wake Strings
                    if "jarvis" in text or "he jarvis" in text or "hey jarvis" in text:
                        self.active_listening = True
                        self.activation_timestamp = current_time
                        self.state_changed.emit("listening")
                        print("🔓 System: JARVIS Active. Listening for command...")
                        
                        # Strip wake words out to see if payload was delivered in same sentence
                        command = text.replace("he jarvis", "").replace("hey jarvis", "").replace("jarvis", "").strip()
                        if command:
                            self.active_listening = False
                            self.text_recognized.emit(command)
                    
                    # Process incoming text payload only if the system is awake
                    elif self.active_listening:
                        self.active_listening = False  # Lock back down instantly upon receiving command
                        self.text_recognized.emit(text)