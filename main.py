import googletrans
import playsound
import speech_recognition as sr
#import pyaudio
import gtts

# USE THE MICROPRHONE
recognizer = sr.Recognizer()

# CREATE A TRANSLATOR
translator = googletrans.Translator()
input_language = 'it-IT'
output_language = 'fr'

try:
    with sr.Microphone() as source:
        print('speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice,language=input_language)
        print(text)
except:
    pass

translated = translator.translate(text,dest=output_language)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_language)
converted_audio.save('audio-translation.mp3')
playsound.playsound('audio-translation.mp3')
#print(googletrans.LANGUAGES)
