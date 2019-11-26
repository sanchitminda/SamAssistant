
import pyttsx3
import speech_recognition as sr
import json
import playsound
from gtts import gTTS
import random
import os
import Detectorr
from pydub import AudioSegment

list_of_variables = ['.user.','.date.','.time.']
list_of_commands = {}

def say(s):
    print('SSAM : ' + s)

    sound = AudioSegment
    for x in s.split():
        paxx = 'SpeechData\\'+x+'.mp3'
        print(paxx)
        if os.path.exists(paxx):
            DS= open(paxx,'r')
            c = AudioSegment.from_mp3(paxx)
            sound = sound + c

        else:
            gTTS(text=x, lang='hi').save(paxx)
            c = AudioSegment.from_mp3(paxx)
            sound = sound + c
    sound.export('SpeechData\\' + 'temp' + ".mp3")
    playsound.playsound('SpeechData\\' + 'temp' + ".mp3")
def say_n_listen(s):
    say(s)
    return listen_audio()


def listen_audio():
    # get audio from the microphone
    print("wait")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        print("Speak!!!")
        audio = r.listen(source)
        print("processing...")
        # print(r.)
        # r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")

    try:
        speech = r.recognize_google(audio)
        print("You : " + speech)
        return speech
    except sr.UnknownValueError:
        return "Could not understand audio"
        return ''
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return 'sorry can\'t reach the internet'


current_answer = 0
q = []
fin = 0
def refresh_file():
    fin = open('QB.dat', 'r')
    for n in fin:
        simple_json = json
        s = simple_json.loads(n)
        q.append(s)
    fin.close()

refresh_file()
engine = pyttsx3.init()

while 1:
    user = Detectorr.get_face()
    main_command = listen_audio()
    current_answer = {'Question':'','Answer':'','command':''}
    if main_command == 'bye':
        say('Have a nice day, Master')
        break
    if main_command == '':
        say('Please Say something')
    for x in q:
        if x['Question'].upper() == main_command.upper():
            current_answer = x
    if current_answer in q:
        if current_answer['command'].find('.user.') != -1:
            current_answer['command'] = current_answer['command'].replace('.user.', user)
        if current_answer['Answer'].find('.user.') != -1:
            current_answer['Answer'] = current_answer['Answer'].replace('.user.', user)
        if current_answer['Question'].find('Open') != -1:
            current_answer['Answer'] = 'The work is under construction here'
        say(current_answer['Answer'])
        if current_answer['command'] == '':
            pass
        else:
            os.system(current_answer['command'])
    else:
        say('Sorry I dont know the answer')
        say('would you like to teach me just say yes or no')
        choise = listen_audio()
        if choise == 'yes':
            qna = {'Question': main_command, 'Answer': say_n_listen('Enter the answer of the question'),
                   'command': ''}
            out = open('QB.dat', 'a')
            simple_json = json
            n = simple_json.dumps(qna)
            out.write(n)
            out.write('\n')
            out.close()
            refresh_file()
            pass
        elif choise == 'no':
            continue
        else:
            say('Sorry you have to respose in yes or no')

