import pyttsx3, datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

recognizer = sr.Recognizer()

# print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def TextToSpeech(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def wishme():         # A method to start the conversation
    t = datetime.datetime.now().hour
    greet = ''
    if 4 <= t < 12:
        greet = "Good Morning!"
    elif 12 <= t <= 16:
        greet = 'Good Afternoon!'
    elif 16 < t <= 21:
        greet = 'Good Evening!'
    else:
        greet = 'Hello!'
    
    TextToSpeech(f'{greet} I am Auxiliobits\' AI Receptionist. ')

def SpeechToText():
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 2              # if there's no speech detected for x second, the recognizer will consider the speech input as complete
        audio = recognizer.listen(source)
        try:
            print('Recognizing...')
            query = recognizer.recognize_google(audio, language='en_in')
            print(f'User said: {query}')
        except Exception as e:
            print(e, '\nCouldn\'t recognize, please try again.')
            return None
        return str(query)
    
def Validate_Output(input):
    if input.lower() == 'none':
        raise ValueError('A very specific bad thing happened.')
    