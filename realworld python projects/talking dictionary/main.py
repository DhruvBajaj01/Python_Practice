#imported necessary packages
import pyttsx3
from PyDictionary import PyDictionary
import datetime

#for speak function
engine=pyttsx3.init("sapi5")
#sapi5 helps to enhance sppech-text recognition
#get some properties of pyttsx3
voices=engine.getProperty('voices')
engine.getProperty('rate')
engine.getProperty('volume')
#change the rate of reading a/q to you  
# suggestion : put it <150
engine.setProperty('rate', 165)
#this changes the volume level 
engine.setProperty('volume',200 )
engine.setProperty('voices' , voices[0].id)

#function to speak the given 'audio' parameter
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function to wish/greet user according to time
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour>12:
        speak("Good morning sir Please enter the word to get meaning")

    elif hour<12 and hour>18:
        speak("Good afternoon sir Please enter the word to get meaning")

    else:
        speak("Good evening sir Please enter the word to get meaning")


def meaning(word):
    #creating instance of PyDictionary
    dict = PyDictionary()
    meaning=dict.meaning(word)
    try:
        #iterating the value return by 'meaning' dictionary
        noun_meaning=meaning['Noun'][0]
        print(f'{word} means {noun_meaning}')
        speak(f'{word} means {noun_meaning}')

    except Exception as e:
        speak('unable to get the meaning please try another word')
        print('unable to get the meaning.please try another word')
    

wish()
while True:
    word=input('Please enter the word to get meaning : \n')
    if word!='':
        meaning(word)
    else:
        speak('please enter something to continue...')