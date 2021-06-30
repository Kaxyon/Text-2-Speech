from gtts import gTTS

from playsound import playsound

audio = 'speech.mp3'

language = 'en'

text = input("Enter your text : ")

sp = gTTS(text, lang=language, slow=False)

sp.save(audio)
playsound(audio)