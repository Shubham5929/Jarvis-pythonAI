import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os  
import sys
import subprocess
import time
from googletrans import Translator
import smtplib
import psutil    
from os import system

translator = Translator()
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices[2].id)
Assistant.setProperty('voices', voices[2].id)


def speak(audio):
    Assistant.say(audio)
    Assistant.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning, sir.")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, sir.")

    else:
        speak("Good Night, sir.")

    speak("Hello, I am Jarvis. Please tell me how may I help you.")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-In")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com',587 )
        server.ehlo()
        server.starttls()
        with open("file.txt","r") as f:
            myPassword = f.read()
        server.login('vantechshu6205@gmail.com',myPassword)
        server.sendmail('vantechshu6205@gmail.com',to,content)
        server.close()


if __name__ == '__main__':
    # speak("Shubham is a good boy.")
    wishMe()
    while True:
        query = takeCommand().lower()

    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open Youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'stop' in query:
            webbrowser.open(exit())
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\New Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the Time is {strTime}")
        elif 'go offline' in query:
            sys.exit()
        elif 'start' in query:
            subprocess.run('start /wait python friday.py', shell=True)

        elif 'open notepad' in query:
            print('What will be the name of your new file')
            speak('What will be the name of your new file')
            time.sleep(5)
            filename = takeCommand().lower()
            speak("Your filename will be " + filename)
            print("Your filename will be " + filename)
            # cmd = f"notepad.exe {filename}.txt"
            # osCommandString = cmd
            # os.system(osCommandString)
            with open(f"{filename}.txt", "w") as f:
                f.write(" ")
            speak('Now Listening please tell me what you want to write in it')
            time.sleep(3)

            text = ""
            while 1:
                text = text + " " + takeCommand().lower()
                if 'stop' in text:
                    break

            text = text[:-5]
            with open(f"{filename}.txt", "w") as f:
                f.write(text)
            speak(
                f"Your content has been successfully written in {filename}.txt")
            print(f"Your content has been successfully written in {filename}")

        # create any file
        elif 'create file' in query:
            print("Please tell me your file name with it's extension")
            speak("Please tell me your file name with it's extension")
            time.sleep(5)
            filename = takeCommand().lower()
            speak("Your filename will be " + filename)
            print("Your filename will be " + filename)
            with open(f"{filename}", "w") as f:
                f.write(" ")
            speak('Now Listening please tell me what you want to write in it')
            time.sleep(3)

            text = ""
            while 1:
                text = text + " " + takeCommand().lower()
                if 'stop' in text:
                    break

            text = text[:-5]
            with open(f"{filename}", "w") as f:
                f.write(f"print(\"{text}\")")
            speak(f"Your content has been successfully written in {filename}")
            print(f"Your content has been successfully written in {filename}")

        # execute
        elif 'execute' in query:
            print("Please tell me the file name with extension you want to execute")
            speak("Please tell me the file name with extension you want to execute")

            # filename = takeCommand().lower()
            subprocess.run(f'start /wait python hello.py', shell=True)

            # print(f"Your filename is {filename}")
            # try :
            # except Exception as e:
            #     print(e)
            #     speak(f"Your file doesn't exists {filename}")

        elif 'read file' in query:
            print("Please tell me your file name that you want me to read")
            speak("Please tell me your file name that you want me to read")
            filename = takeCommand().lower()
            with open(f'{filename}.txt','r') as f:
               text = f.read()
               print(text)
            speak(text)
        # elif 'translator' in query:
        #     print("Please tell me what you want to translate")
        #     speak("Please tell me what you want to translate")
        #     # speech = takeCommand().lower()
        #     translations = translator.translate("thunder bird", dest='en')
        #     print(translations.text)
        #     speak(translations.text)
        
        elif 'open code' in query:
            codePath = "D:\\visual studio file\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email' in query:
            try:
                 speak("Whom you would like to send to")
                 to = takeCommand().lower()
                 speak("What would you like to send")
                 content = takeCommand().lower()

                 sendEmail(to,content)
                 speak("Email has been sent!")
                 print("Email has been sent!")
            except Exception as e:
                print(e)
                print('Sorry my friend shubham. I am not able to send this email.')
        elif 'shutdown' in query:
            print('Are you sure to shut down the computer?(Yes/No): ')
            speak('Are you sure to shut down the computer?(Yes/No): ')
            shutDown = takeCommand().lower()
            try:
                if shutDown == "yes":
                   print("yes")
                   os.system("shutdown /s /t 1")
                else:
                   exit()
            except Exception as e:
                print(e)
                speak(f'here this is your {e} error occurs. So, please check you code!')
        
        elif 'restart' in query:
            print('Are you sure to restart the computer?(Yes/No): ')
            speak('Are you sure to restart the computer?(Yes/No): ')
            # Restart = takeCommand().lower()
            # if Restart == "yes":
            #    print("yes")
            os.system("shutdown /r /t 1")
        
        elif 'kill app' in query:
            print("Are you sure to kill the task?(Yes/No): ")
            speak("Are you sure to kill the task?(Yes/No): ")
            while True:
                Sure = takeCommand().lower()
                try:
                    if Sure == "yes":
                        print("What is your name of app? ")
                        speak("What is your name of app? ")
                        appName = takeCommand().lower()
                        subprocess.call(["taskkill","/F","/IM",appName])
                        speak("Your task of app is closed successfully now!")
                    else:
                        break
                except Exception as e:
                    print(f'this is your {e} error occurs.')

            
               

