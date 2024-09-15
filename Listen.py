import speech_recognition as sr 

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4) 
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")

    except Exception as e:
        print("Say Again")
        return "None"
    
    query = str(query).lower()
    return query



def MicExecution():
    query = Listen()
    return query

