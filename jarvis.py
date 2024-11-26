import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice. You can change index to use other voices.

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greet the user based on the time of the day."""
    hour = int(datetime.datetime.now().hour)
    print(f"Current hour: {hour}")  # Debugging line to check the current hour
    
    if hour >= 0 and hour < 12:
        print("It's morning.")
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("It's afternoon.")
        speak("Good Afternoon!")
    else:
        print("It's evening.")
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    """
    Listen for the user's command.
    Returns the command as a string.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    """
    Send an email.
    You need to enable 'less secure apps' on your email account for this to work.
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email")

if __name__ == "__main__":
    # Register Chrome as the web browser
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'open youtube' in query:
            webbrowser.get('chrome').open("http://youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("http://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("http://stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\Desktop\\websites"
            os.startfile(codePath)

        elif 'email to Zohair' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "syedzohair@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
        else:
            print("No query matched")
