import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Command keywords
GREETING_KEYWORD = "hello"
WEATHER_KEYWORD = "what's the weather"
GOODBYE_KEYWORD = "goodbye"
EXIT_KEYWORD = "exit"
TIME_KEYWORD = "what's the time"
OPEN_KEYWORD = "open"
INTRODUCTION_KEYWORD = "introduce yourself"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)

            # Process voice command
            if GREETING_KEYWORD in command.lower():
                speak("Hello! How can I assist you?")
            elif WEATHER_KEYWORD in command.lower():
                speak("I'm sorry, I cannot provide weather information at the moment.")
            elif GOODBYE_KEYWORD in command.lower():
                speak("Goodbye! Have a great day.")
                exit()  # Exit the program gracefully
            elif EXIT_KEYWORD in command.lower():
                speak("Exiting the program. Goodbye!")
                exit()  # Exit the program gracefully
            elif TIME_KEYWORD in command.lower():
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}.")
            elif command.lower().startswith(OPEN_KEYWORD):
                # Extract the website name from the command
                website = command[len(OPEN_KEYWORD):].strip()
                url = f"https://www.{website}.com"
                try:
                    webbrowser.open(url)
                    speak(f"Opening {website}.")
                except Exception as e:
                    speak(f"Sorry, I couldn't open {website}.")
            elif INTRODUCTION_KEYWORD in command.lower():
                speak("I am your virtual assistant. I can provide information, open websites, and more. How can I assist you?")
            else:
                speak("I didn't understand your command. Please try again.")

        except sr.WaitTimeoutError:
            print("Timeout. Please speak again.")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    speak("Welcome! How can I assist you?")
    while True:
        process_command()
