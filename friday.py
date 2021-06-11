import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # use voices[0] to get male voice


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                print('listening...')
                command = command.replace('friday', '')
                print(command)
                call_friday(command)
            else:
                pass
    except:
        pass


def call_friday(command):
    if 'are you there' in command:
        fine = "I am always here for you, you can call me by using the name 'Friday' "
        print(fine)
        talk(fine)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        date = str(date)
        print('Today\'s date is ' + date)
        talk('Today\'s date is ' + date)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'how are you' or 'are you fine' in command:
        fine = "I am fine, how may I help you"
        print(fine)
        talk(fine)
    elif 'who is' or 'tell me about' in command:
        person = command.replace('who is', '')
        person = command.replace('tell me', '')
        person = command.replace('about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('Sorry, i cant understand you.')


print("running...")
welcome = "welcome back sir, I am here to help you, you can call me by name friday"
print(welcome)
talk(welcome)
while True:
    listen()

