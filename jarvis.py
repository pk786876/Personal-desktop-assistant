import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import random
import cv2
import sys
import pyautogui
import time
import operator
import requests
from AppOpener import open ,close


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voic',voices[0].id)
engine.setProperty('rate',130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!, sir")   
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!, sir")  
        
    else:
        speak("Good Evening!, sir") 
        
    speak("Ready To Comply. What can I do for you ?")         
    
def takeCommand():
     
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
        
    try: 
        print("Recognizing...")   
        query = r.recognize_google(audio, language='en-in')
        print(f'user said :(query)\n')
        
    except Exception as e:
        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            print("yes sir")
            speak("yes sir")
            
        elif "who are you"  in query:
            print('my name is jarvis')  
            speak('my name is jarvis')
            print('I can do everything that  my creater programmed me to do') 
            speak('I can do everything that  my creater programmed me to do')
            
        elif "who create you" in query:
            print('I do not know his name, I created with python language, in v.s code')   
            speak('I do not know his name, I created with python language, in v.s code')  
            
        elif 'what is' in query:
            speak('searching wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'who is' in query:
            speak('searching wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)    
            
        elif 'just open google' in query:
            speak("Open google sir ...")
            webbrowser.open('https://google.com')  
            
        elif 'open google' in query:
            speak("what should I search ?")    
            qry = takeCommand().lower()
            wk.playonyt(f"{qry}")
            #webbrowser.open(f"{qry}")
            
            
            
        elif 'search on google' in query:
            query = query.replace("search on google", "")   
            webbrowser.open_new_tab(f"https://www.google.dz/search?q={query}")
               
            
        elif 'just open youtube' in query:
            speak("Open Youtube sir...")
            webbrowser.open('https://Youtube.com')
            
        elif 'open youtube' in query:
            speak("what you will like to watch ?")    
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")
                    
        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")   
            webbrowser.open_new_tab(f"www.youtube.com/results?search_query={query}")
            
        elif 'close browser' in query: 
            os.system("taskkill /f /im msedge.exe")        
                
        elif 'close chrome' in query: 
            os.system("taskkill /f /im chrome.exe")  
##            
        elif "play music" in query:
            music_dir = 'E:\Musics'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))     
                 
        elif "open word" in query:
            npath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(os.path.normpath(npath))             
                              
        elif "close word"  in query:
            os.system("taskkill /f /im") 
            
        elif "open whatsapp" in query:
            open("whatsapp")
            
        elif "close whatsapp" in query:
            close("whatsapp")   
            
        elif "open instagram" in query:
            open("instagram")
            
        elif "close instagram" in query:
            close("instagram")       
 ##           
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"sir, the time is {strTime}")  
            
        elif "shutdown the system"  in query:
            os.system("shutdown /p")        
            
        elif "restart the system"  in query:
            os.system("shutdown -t 0 -r -f")    
            
        elif "lock the system"  in query:
            os.system("rundll32.exe user32.dll, LockWorkStation")   
            
        elif "hibernate the system"  in query:
            os.system("shutdown.exe /h")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyAllWindows()
                
        elif "go to sleep" in query:
            speak("alright then, i am switching off")
            sys.exit()
            
        elif "take screenshot" in query:
            speak("tell me the name for the file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")   
            
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{ 
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'div' : operator.__truediv__,
                    }[op]
                def eval_bianary_expr(op1, oper, op2):
                    op1,op2 =  int(op1), int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak("your result is")
                speak(eval_bianary_expr(*(my_string.split())))     
                
        elif "my I.P address" in query:
            speak("checking")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                speak("your ip address is ")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak try again later")
                
        elif  "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            
        elif "volume down" in query:
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")              
            pyautogui.press("volumedown")              
            pyautogui.press("volumedown")           
            pyautogui.press("volumedown")              
            pyautogui.press("volumedown")             
            pyautogui.press("volumedown")             
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")  
            pyautogui.press("volumedown")  
            
        #elif "mute" or "unmute" in query:
            #pyautogui.press("volumemute")  
            
              
              
                  
                    
                    
                
                
                    
                                                                       