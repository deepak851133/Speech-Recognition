import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize Recognizer and TTS engine globally
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    """Function to process user commands"""
    c = c.lower()  # Fix: Correct variable reference

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open news" in c or "show news" in c:
        webbrowser.open("https://news.google.com")
   
        
if __name__ == "__main__":
    speak("Initializing voice assistant...")

    while True:
        print("Waiting for wake word: 'google'...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for noise
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            word = recognizer.recognize_google(audio)
            print(f"Recognized: {word}")

            if word.lower() == "google":
                speak("Yes, I am listening.")
                
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("google Active... Speak your command.")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                command = recognizer.recognize_google(audio)
                print(f"Command Recognized: {command}")
                process_command(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")
