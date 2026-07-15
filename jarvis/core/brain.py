# core/brain.py
import os
from dotenv import load_dotenv
from groq import Groq

# Pull files directly from your api.env tracking system
load_dotenv(dotenv_path="api.env")

class JarvisBrain:
    def __init__(self):
        """
        Initializes the Groq inference engine client.
        Looks for the 'GROQ_API_KEY' inside api.env.
        """
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = None
        
        if not self.api_key or "YOUR_API_KEY_HERE" in self.api_key:
            print("⚠️ NOTE: GROQ_API_KEY is currently empty or placeholder text.")
        else:
            try:
                # Initialize the official Groq client connection
                self.client = Groq(api_key=self.api_key)
                print("🛡️ GROQ CORE: Handshake complete. Accelerated hardware token path active.")
            except Exception as init_err:
                print(f"⚠️ INITIALIZATION ERROR: Groq wrapper client failed: {init_err}")

    def query(self, prompt):
        """
        Dispatches voice token text strings straight to Groq for ultra-low latency response vectors.
        """
        # Fallback offline responses if the key hasn't been added yet
        if not self.client:
            user_input = prompt.lower().strip()
            if "hello" in user_input or "jarvis" in user_input:
                return "Offline fail-safe active, sir. Please configure your GROQ_API_KEY inside api.env."
            return "Systems operational, waiting for Groq engine credentials to initialize remote cloud link."

        try:
            # Execute chat completion structure using a production-ready Llama model on Groq
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are JARVIS, a helpful, ultra-fast tactical AI assistant. Keep responses brief and clean."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.6,
                max_tokens=150
            )
            
            # Extract out the returned text content data
            if chat_completion.choices and len(chat_completion.choices) > 0:
                return chat_completion.choices[0].message.content
            else:
                return "Engine failed to parse text from the execution stack."

        except Exception as groq_err:
            print(f"⚠️ GROQ CHAT INFERENCE FAULT: {groq_err}")
            return "An execution pipeline anomaly occurred while fetching neural text weights."