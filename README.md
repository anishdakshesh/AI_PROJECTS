# AI
A python based AI system for PC.

We import the necessary libraries, including SpeechRecognition and pyttsx3. [pip install SpeechRecognition pyttsx3]
We define a speak function to convert text to speech.
The process_command function listens for voice commands using a microphone, recognizes the command using Google's speech recognition service, and then processes the command based on what it recognizes.
We have a simple command recognition system that responds to commands like "hello," "what's the weather," and "goodbye."
The code runs in a loop, continuously listening for voice commands.
