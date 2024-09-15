import pyttsx3

def Speak(Text):
     engine = pyttsx3.init("sapi5")
     voices = engine.getProperty('voices')
     engine.setProperty('voice',voices[0].id)
     engine.setProperty('rate',170)
     print("")
     print(f"You : {Text}.")
     print("")
     engine.say(Text)
     engine.runAndWait()