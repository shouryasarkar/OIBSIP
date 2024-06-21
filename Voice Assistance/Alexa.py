

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os, cv2
import DBUtils

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(e)
    return command


def talk(text):
    engine.say(text)
    engine.runAndWait()



def run_alexa():
    command = take_command()
    print(command)

    if 'favourite' in command:
        print("I am here")
        with open("fav_songs.txt", 'r') as file:
            song_name = file.readlines()
            print(song_name)
            talk("Which song do you want to play from your favourites list? The songs in your list are : ")
            for i,each_song in enumerate(song_name):
                talk_string = "Song number" + str(i+1) + "is" + each_song.strip().replace("\n","")
                talk(talk_string)
            song_choice = take_command()
            if song_choice.strip() in song_name:
                 pywhatkit.playonyt(song_name)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you single' in command:
        talk('I am in a relationship with Kaustuv') 
    elif 'what is my name' in command:
        talk('Your name is Shourya Sarkar')
    elif 'how is your day going' in command:
        talk('Excellent,and yours??')
    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '')
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "shut down" in command:
        if "pc"in command or "computer" in command:
            talk("Powering off your computer")
            os.system("shutdown /s /t 1")
        else:
            talk("I can only shutdown your computer as of now.")
    elif "selfie" in command:
        vid = cv2.VideoCapture(0)
        while (True):
            ret, frame = vid.read()
            if ret:
                name = 'Habla_selfie.jpg'
                print('Creating... ' + name)
                cv2.imwrite(name, frame)
                break
            else:
                break
        vid.release()
        cv2.destroyAllWindows()

    elif "open" in command and "camera" in command:
        vid = cv2.VideoCapture(0)
        while (True):
            ret, frame = vid.read()
            if ret:
                cv2.imshow('camera', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        vid.release()
        cv2.destroyAllWindows()

#JOJO MATOBBORI#

    elif "close" in command and "camera" in command:
        vid = cv2.VideoCapture(0)
        while (True):
            ret, frame = vid.read()
            if ret:
                cv2.imshow('camera', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        vid.release()
        cv2.destroyAllWindows()

#JOJO MATOBBORI#


    elif "send" in command and "whatsapp" in command:
        hour_now = datetime.datetime.now().strftime('%H')
        min_now  = datetime.datetime.now().strftime('%M')
        pywhatkit.sendwhatmsg("+919007762898", "Hello from Habla's Alexa", int(hour_now), int(min_now)+1)
        talk("Whatsapp message sent")
    elif "call" in command:
        first_name = "Pranab"
        last_name  = "Sarkar"
        sql_query = "SELECT phone FROM phonebook WHERE first_name = '%s'" % (first_name,last_name)
        DBcontent = DBUtils.DB_Execute(sql_query, "fetch")
        talk("Showing the number ")
        print("phone no: - ", DBcontent[0][0])



while True:
    run_alexa()
