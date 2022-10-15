#creating alexa 
"""
Important points to consider

1. when we are making alexa speak the next command will execute only when it stops spaekinf or the command is over!
2. if you input additional speeches to apeak the tone to speaking changes while using question mark,explanatory mark and dot.
"""

import speech_recognition as sr
import pyttsx3 # is called "python text to speech" - to get reply from python(alexa).
import pywhatkit  # very important kit to play songs
import wikipedia # to get search results 
import datetime # to get time.

#for fun 
import pyjokes

listener = sr.Recognizer() # it will help  Python(So called alexa) to understand speeches.
engine = pyttsx3.init()

# creating a girl voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

## creating a wecome speech for alexa
# engine.say("Hey I am Alexa")
# engine.say("Say Something?")
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
 
#to overcome exceptions like "absurd speech " ,"disablitiy in speech recognition".
def alexa_in_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # this will create text of our speech that is stored in voice variable.
            command = command.lower()  # to make command to lower case
            if 'alexa' in command:    # to respond only if 'alexa' is used.
                # talk(command)
                command = command.replace('alexa','') # alexa will be replaced from the string.
                print(command); # for our satisfaction.
              
    except:
        pass
    return command

def run_alexa():
    command = alexa_in_command()
    print(command)

    if 'play' in command:
        song =command.replace('play','')
        # print("playing"+ song)
        talk('playing'+song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        date = datetime.date.today()
        
        month = date.strftime("%B") # to get month as name 
        time= datetime.datetime.now().strftime('%d '+month+' %Y '+ 'and Time is '+'%H:%M:%S') # her we can use >> "%I:%M %p" << to get 12 hour format with am pm indication.
        talk('Current date is '+time)
        print(time)
    
    elif 'wikipedia' in command:
        person = command.replace('wikipedia','')
        info = wikipedia.summary(person,1)  # it will search person in wikipedia and willl output 1 line of sentence.
        print(info)
        talk(info)
    
    elif 'himanshu' in command:
        talk('himanshu is a sexy milf')
    
    elif 'joke' or 'jokes' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again ')
    
while True:
    run_alexa()
 