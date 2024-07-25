import speech_recognition as sr
import pyttsx3
import datetime
import requests


# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for a command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, there seems to be an issue with the speech recognition service.")
            return ""

# Function to respond to simple commands
def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        web_search(search_query)
    else:
        speak("Sorry, I did not understand that command.")

# Function to perform a web search
def web_search(query):
    if query:
        speak(f"Searching the web for {query}")
        response = requests.get(f"https://www.google.com/search?q={query}")
        if response.status_code == 200:
            speak("Here are some results I found on the web.")
            # This is a placeholder. Normally, you'd parse the response and provide relevant information.
            print(response.text[:500])  # Print the first 500 characters of the response
        else:
            speak("Sorry, I couldn't fetch the results at the moment.")
    else:
        speak("Sorry, I didn't catch what you want to search for.")

# Main loop
def main():
    speak("Voice assistant activated...Hello Shruti Chandrakar.. How can I assist you?")
    while True:
        command = listen()
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        respond(command)

if __name__ == "__main__":
    main()
