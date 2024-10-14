import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('good afternoon how are you doing')
engine.say('i am your c e c assistant')
engine.say('what can i do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'admission' in command:
        print('please ask your queries in the office room which is in the ground floor of main block')
        talk('please ask your queries in the office room which is in the ground floor of main block')
    elif 'what' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please repeat the command again')


while True:
    run_alexa()