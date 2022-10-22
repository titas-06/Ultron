import speech_recognition as sr
from time import ctime
import webbrowser
import time
import pywhatkit
import pyttsx3
import wikipedia
import os
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
 engine.say(text)
 engine.runAndWait()

r=sr.Recognizer()


def record_audio(ask=False):
 with sr.Microphone() as source:
    if ask:
     print (ask)

    audio = r.listen(source)
    
    try:
     voice_data= r.recognize_google(audio)
     voice_data=voice_data.lower()
     print(voice_data)
    except sr.UnknownValueError:
        print("Sorry, i did not get that....")
        talk("Sorry, i did not get that....")
    except sr.RequestError:
        print("System error.....")
        talk("System error.....")
 return voice_data

def respond(voice_data):
      if 'what is your name' in voice_data:
          print("My name is Jarvis")
          talk("My name is Jarvis")

      elif 'what is' in voice_data:
          voice_data = voice_data.replace('what is', '')
          info = wikipedia.summary(voice_data,  4)
          print(info)
          talk(info)

      elif 'wikipedia' in voice_data:
          voice_data = voice_data.replace('wikipedia', '')
          info = wikipedia.summary(voice_data, 4)
          print(info)
          talk(info)

      elif 'time'in voice_data:
          print(ctime())
          talk(ctime())

      elif 'search' in voice_data:
        if (len(voice_data)==6):
          talk('What do you want to search')
          search=record_audio('What do you want to search')
          url='http://google.com/search?q='+search
          webbrowser.get().open(url)
          print('Sir,here is what i found')
          talk('Sir,here is what i found')
          info = wikipedia.summary(search, 2)
          print(info)
          talk(info)
        else:
          search = voice_data.replace('search', '')
          url='http://google.com/search?q='+search
          webbrowser.get().open(url)
          print('Sir,here is what i found')
          talk('Sir,here is what i found')
          info = wikipedia.summary(search, 2)
          print(info)
          talk(info)

      elif'who is' in voice_data:
          voice_data=voice_data.replace('who is','')
          info=wikipedia.summary(voice_data, 4)
          print(info)
          talk(info)

      elif 'find location' in voice_data:
          location=record_audio('What is the location')
          url='http://google.nl/maps/place/'+location+'/&amp;'
          webbrowser.get().open(url)
          print('Sir,opening maps')
          print('Sir,opening maps')
      elif 'location' in voice_data:
              location = voice_data.replace("location","")
              url = 'http://google.nl/maps/place/' + location + '/&amp;'
              webbrowser.get().open(url)
              print('Sir,opening maps')
              talk('Sir,opening maps')

      elif'open youtube' in voice_data:
          url = 'https://www.youtube.com'
          webbrowser.get().open(url)
          print('Opening youtube..')
          talk('Opening youtube..')

      elif 'play' in voice_data:
          song=voice_data.replace('play','')
          pywhatkit.playonyt(song)
          talk('playing'+song)

      elif 'whatsapp' in voice_data:
          url='http://web.whatsapp.com'
          webbrowser.get().open(url)
          print("Opening whatsapp")
          talk("Opening whatsapp")

      elif 'facebook' in voice_data:
          url = 'https://www.facebook.com/'
          webbrowser.get().open(url)
          print("Opening facebook")
          talk("Opening facebook")

      elif 'instagram' in voice_data:
          url = 'https://www.instagram.com/'
          webbrowser.get().open(url)
          print("Opening instagram")
          talk("Opening instagram")

      elif 'open teams' in voice_data:
          path="C:\\Users\\Titas Sikdar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.lnk"
          print('opening microsoft teams')
          talk('opening microsoft teams')
          os.startfile(path)

      elif 'open word' in voice_data:
          path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
          print('opening microsoft word')
          talk('opening microsoft word')
          os.startfile(path)

      elif 'open powerpoint' in voice_data:
          path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
          print('opening microsoft powerpoint')
          talk('opening microsoft powerpoint')
          os.startfile(path)

      elif 'exit' in voice_data:
          exit()

time.sleep(2)
print("Hello sir .. Jarvis here How may i help you....")
talk("Hello sir .. Jarvis here How may i help you")
while 2:
 voice_data=record_audio()
 respond(voice_data)