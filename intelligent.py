from brain6 import ReplyBrain
from Listen import MicExecution

def MainExecution():

    from Speak2 import Speak
    Speak("Initiating the bail reckoner!")
    Speak("Everything operational sir!")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")
        Reply = ReplyBrain(Data)
        Speak(Reply)
           
MainExecution()





