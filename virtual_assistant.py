import speech_recognition as sr
import playsound
import random
from gtts import gTTS # google text to speech
import webbrowser
import ssl
import certifi
import time
import os  # remove the audio files
import subprocess
from PIL import Image
import pyautogui  # screenshot
import pyttsx3
import bs4 as bs
import urllib.request
from time import ctime
from subprocess import call

class person:
    name=''
    def setName(self,name):
        self.name=name
class assist:
    name=''
    def setName(self,name):
        self.name=name
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
def engine_speak(text):
    text =str(text)
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer()  ## initialise the recognizer , listen for audio and convert it to tet
def record_audio(ask=""):
    with sr.Microphone() as source:    # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source,8,8)
        print("Done listening")
    data = ""
    try:
        data = r.recognize_google(audio)  # convert audio to text
        print("You said: " + data)
    except sr.UnknownValueError: # error:recogniser does not understand
        engine_speak("Sorry sir,did not get what you have said")
        #print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e: 
        engine_speak("Sorry the server is down") # error the reconizer is not connected
        print("Request Failed; {0}".format(e))#
    return data.lower()
    
    # get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string=str(audio_string)
    tts=gTTS(text=audio_string,lang='en')  #text to speech
    r=random.randint(1,20000000)
    audio_file='audio'+str(r)+'.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # help us to play the audio
    print(assist_obj.name+':',audio_string) # print what app said
    os.remove(audio_file) # Remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if assist_obj.name:
            engine_speak("whats with my name "+assist_obj.name)
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        assist_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        pyttsx3.speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search for","search"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    #7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    #8: search for music
    if there_exists(["play music","play"]):
        search_term= voice_data.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to"+ search_term +"enjoy sir")
    #9: search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.amazon.in"+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")
         
    #10: make a note
    if there_exists(["make a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")
    
    # 11: open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")
        
    #12: delopen twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")

    #13: time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()
    
    #14: weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
    
    #15: open gmail
    if there_exists(["open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")

    #16: stone paper scisorrs
    
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")   
        
    #17: toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

    #18: calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

    #19: screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:\\Users\\ROCK_7\\OneDrive\Pictures\\Screenshots') 
    
    
    #20: to search wikipedia for definition
    if there_exists(["definition of"]):
        definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found '+definitions[1])
            else:
                engine_speak ('Here is what i found '+definitions[2])
        else:
                engine_speak("im sorry i could not find the definition for "+definition)
    #21: open apps
    elif there_exists(["whatsapp"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Whatsapp")
        print(".")
        print(".")
        call(('cmd', '/c', 'start', '', 'C:/Users\ROCK_7/AppData/Local/WhatsApp/whatsapp.exe'))

    elif there_exists(["google","search","browser","web browser","chrome"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("GOOGLE CHROME")
        print(".")
        print(".")
        # file='"C:\Program Files\Google\Chrome\Application\google chrome.exe"'
        # os.system(file)
        webbrowser.get().open("https://www.google.com/")

    elif there_exists(["ie","msedge","edge"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT EDGE")
        print(".")
        print(".")
        #os.system("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        call(('cmd', '/c', 'start', '', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'))

    elif there_exists(["notes","note","notepad","editor"]):
        pyttsx3.speak("NOTEPAD")
        print(".")
        print(".")
        call(('cmd', '/c', 'start', '', 'C:/Windows/system32/notepad.exe'))

    elif there_exists(["vlcplayer","player","video player"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("VLC PLAYER")
        print(".")
        print(".")
        call(('cmd', '/c', 'start', '', 'C:/Program Files (x86)/VideoLAN/VLC/vlc.exe'))

    elif there_exists(["telegram","TG"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("TELEGRAM")
        print(".")
        print(".")
        call(('cmd', '/c', 'start', '', 'C:/Users/ROCK_7/AppData/Roaming/Telegram Desktop/telegram.exe'))

    elif there_exists(["excel","msexcel","sheet"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT EXCEL")
        print(".")
        print(".")
        call(('cmd', '/c', 'start', '', 'C:/Program Files/Microsoft Office/root/Office16/excel.exe'))
 
    elif there_exists(["slide","mspowerpoint","ppt"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT POWERPOINT")
        print(".")
        print(".")
        os.system("start ppt3.pptx")
 
    elif there_exists(["word","msword"]):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT WORD")
        print(".")
        print(".")
        os.system("start python.docx")

    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("we could continue more sir, but.,,...,,,,,..,,,,, byee")
        exit()

time.sleep(1)

person_obj = person()
assist_obj = assist()
assist_obj.name = 'Jarvis'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond

    # text =str(text)
    # engine.say(text)
    # engine.runAndWait()


  

