import tkinter as tk
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import fnmatch,glob
import subprocess
import pyttsx3
import speech_recognition
import threading
import multiprocessing
from multiprocessing import Queue
from PIL import ImageTk,Image
import webbrowser
#import pygame
import pyscreenshot#need to install pillow before
import datetime
import playsound
from tkinter.filedialog import askopenfile, asksaveasfilename
from cv2 import *
import time













data_list=[ "Hi what's your name?",
            'My name is Thursday',
            'I am your personal assistant',
            'You can ask me anything you want',
            'I say no only if no is required',
            'My favourite character is Motto Motto from Madagascar 2',
            'I was named Thursday as I was born on a Thursday',
            'I would eat meat if I could eat',
            'I love to learn new stuff, would you like to teach me something',
            'I am usually calm, depending on the question',
            'Please dont ask me if god exists, I am tired of that question',
            "I like lamborghini",
        
            ]








bot=ChatBot('Bot')
trainer=ListTrainer(bot)

#for files in os.listdir('data/english/'):
     #data=open('data/english/'+files,'r',encoding='utf-8').readlines()
     #trainer.train(data)
     
trainer.train(data_list)   
     
     

      
            
            
            

     
     
     
def open_desktop_app(application):#hanging,used for getting the path of the specified file
        for root,dirs,files in os.walk('/'):
            for file in files:
                if glob.fnmatch.fnmatch(file,application):
                    print(os.path.abspath(file))
                    path = os.path.abspath(os.path.join(root, file))
                    global answer 
                    answer = path
                    #print(path)
        #subprocess.Popen(path)
        #os.system('brave')
        #subprocess.check_call(path,'program')
        #vpath = 'C:\\Windows\\System32\\notepad.exe'
        #subprocess.run([sys.executable,vpath])
        #return path 


            
            
            




def first_response():#not working,wanted to say it as a greeting
    
    first_reply='Hi i am Thursday....... I am your personal assistant, what can I do for your'
    textarea.insert(END,'Bot: '+str(first_reply)+'\n\n')
    pyttsx3.speak(first_reply)
    

#first_response()











def open_web(name):#opens the link in a web browser
    try:
        web = 'www.'+str(name)+'.com'
        webbrowser.open(web)
        global answer
        answer = 'opening '+str(name)+'....please wait for a moment'
    except Exception as e:
        print(e)
        answer = 'I am sorry i was unable to open '+str(name)


            
            
            
#trainer.train(data_list)
#engine = pyttsx3.init()










def date_and_time():
    #gives the current date and time 
    now = datetime.datetime.now()
    time_now_string = now.strftime("%#d %#B %#Y-%#I:%#M%p")
    global answer 
    answer = "It is "+time_now_string
    textarea.insert(END,'Bot: '+answer+'\n\n')
    pyttsx3.speak(answer)
    
    
  
  





  
    
    
def date_today():
    
    #gives the current date
    today = datetime.date.today()
    day_string = today.strftime("%d %B, %Y")
    global answer 
    answer= "It is "+day_string
    textarea.insert(END,'Bot: '+answer+'\n\n')
    pyttsx3.speak(answer)
    
    




            
            
            
            

def screen_shot():
    
    
    #takes the screenshot and saves the file as the current date
    root.iconify()#minimizes the tk window
    today = datetime.date.today()
    now = datetime.datetime.now()
    day_string = today.strftime("%d %B, %Y")
    time_now_string = now.strftime("%#d %#B %#Y-%#I:%#M%p")
    

    try:
        image = pyscreenshot.grab()
        image_name ='screenshot '+day_string+'.png'
        time.sleep(5)
        image.save(image_name)
        global answer
        answer = 'opening screenshot....please wait for a moment'
    
        image.show(image_name)
    except Exception as e:
        answer = 'I was not able to save the image due to '+str(e)
    
 
 
 
 
 




   
   
def take_pic():
    
    
    #takes a pic and then helps us to save it in a desired manner
    global answer
    answer = 'taking your picture smile please....'
    textarea.insert(END,'Bot: '+answer+'\n\n')
    pyttsx3.speak(answer)
                
    
    cam = VideoCapture(0,cv2.CAP_DSHOW)   # 0 -> index of camera
    s, img = cam.read()
    
    if s:    # frame captured without any errors
        namedWindow("cam-test")
        imshow("cam-test",img)
        waitKey(0)
        #time.sleep(5)
        destroyWindow("cam-test")
        try:
            
            answer = 'saving picture of yours ....hang on for a moment'
            filename =  asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("png file","*.png"),))
            
            if filename:
                name = filename.split('.')
                name1= name[0]+'.png'
                print(name1)
                #name = name+'.png'
            
                imwrite(name1,img) #save image
                imshow(name1,img)
                waitKey(0)
                #subprocess
                destroyWindow('img')
                
        except AttributeError:
            
             answer = 'file not saved..... please select a where to save the file'
            
           
    

            
            
            
            




song_path = ''

def play_song():
    
    
    #plays the choosen song from the desired folder,
    
    global song_path
    global answer
    answer = 'opening your favourite song....select the file please'
    textarea.insert(END,'Bot: '+answer+'\n\n')
    pyttsx3.speak(answer)
                
    
    try:
        song_path = askopenfile(filetypes = [("mp3 files","*.mp3")])
        print(song_path)
        #if song_path:
        song_path = song_path.name
        song = song_path.split('.')
        song = song[0]+'.mp3'
        song = str(song)
        playsound.playsound(song)
        
    except (AttributeError, playsound.PlaysoundException):
       
        answer = "there was some problem i couldn't load the song"
    
#answer = 'Hi my name is Thursday, I am your personal assistant'











def botReply():
    
        #gives the response from the personal assistant
        question=questionField.get()
        question=question.capitalize()
        response=bot.get_response(question)
        textarea.insert(END,'You: '+question+'\n\n')
        #textarea.insert(END,'Bot: '+str(response)+'\n\n')
                
        #pyttsx3.speak(response)
        opener = question.split(' ')
        
        
        #print(opener)
        
        
        
        
        
        


        
        try:
            answer =''#'Hi I am Thursday, your personal assistant.What can i do for you??'(not working)
            if len(opener)>1:
            
                #if opener[0]=='open' or opener[0]=='Open':
                
                if 'open' or 'Open' in opener:
                            
                    if opener[1]=='application':
                        
                        #if we give a command like "open application notepad", it opens up notepad.like that many desktop apps
                        
                            cmd = opener[-1].capitalize()#+'.exe'
                            #open_desktop_app(cmd)
                            os.system(cmd)
                            answer = 'opening the application '+str(cmd)
                            #opens spotify,notepad,
                        
                        
                    
                #if 'open' or "Open" and 'website' in opener:
                    elif opener[1]=='website':  
                        
                        
                        #Command="open website google,amazon,"etc. calls the function to open websites
                        
                        web = opener[-1]
                        open_web(web)
                        
                        
                
                if opener[0]=='take' or  opener[0]=='Take':
                    
                    if opener[-1]=="screenshot" or opener[-1]=='Screenshot':
                        
                        
                         #Command="Take screenshot" or "take screenshot".It is used for calling the function to take screenshot
                        screen_shot()
                        
                        
                #if 'take' or 'Take' and 'pic' or 'picture' in opener:        
                    
                        
                    if opener[-1]=='pic' or opener[-1]=='picture':
                        
                        
                         #Command="take pic" or "take picture".It is used for calling the function to take picture from the webcam
                        take_pic()
                    
                    
                    
                
                #elif 'play' or 'song' or 'Play' in opener:
                
                if opener[0]=='play'  or opener[0]=='Play' and  opener[-1]=='song':  
                
                
                
                    #calls the function to play the song.Command="play song"
                    play_song()
                    
                    
                if opener[0]=='date' or opener[0]=='Date':
                    
                    if opener[-1]=='today':
                        
                        
                        #Command="date today or like date of today"
                        date_today()
                        
                        
                    elif opener[-1]=='time':
                        
                        #command="date and time "
                        date_and_time()
                        
                if opener[0]=='give' or opener[0]=='Give' and opener[1]=='path':
                    
                    
                    application = opener[-1]
                    
                    #open_desktop_app(application)  #hangs alot
                    
                        
        
            textarea.insert(END,'Bot: '+ answer +'\n\n')
            pyttsx3.speak(answer)
                
                        
        except (IndexError,IOError,ValueError,TypeError,Exception):
            print('an error  has occured')
            
            answer = 'an error has occured now,please be patient'
                
        
                    
            
                
                        
                        
                        
                        
                        
                        
        #answer = 'Opening '+str(opener[-1])+ '.........please wait'
        answer = ""#"Carry on don't you have anything else to ask me."
            
            
        #textarea.insert(END,'Bot: '+ answer +'\n\n')
        #pyttsx3.speak(answer)
                
        
                
        #except Exception as e:
        #    print(e)
                
        



        textarea.insert(END,'Bot: '+str(response)+'\n\n')
                
        pyttsx3.speak(response)
        
        questionField.delete(0,END)














def audio_text():
    
    while True:
        speech = speech_recognition.Recognizer()
        
        
        try:
            
            with speech_recognition.Microphone() as m:
                speech.adjust_for_ambient_noise(m,duration=0.2)
                audio = speech.listen(m)
                query = speech.recognize_google(audio)
                #query = query.capitalize()
                questionField.delete(0,END)
                questionField.insert(0,query)
                botReply()
                
        except Exception as e:
            print(e)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       







       
       
       
       
       




###############################################################   Tkinter Part   ###################################################




















root=tk.Tk()

root.geometry('500x700')
root.title('            Thursday- Your Personal Assistant')
root.config(bg='indigo')











background_image = PhotoImage(file='wallpaper screenshot red.png')#add the desired image over here wallpaper screenshot3

background_label = Label(root, image = background_image,border=0, height = 1500, width  = 1500, padx  =  10, pady  = 10)

background_label.place(x=0, y=0, relwidth=1,bordermode = INSIDE, relheight = 1, anchor = NW)












pic_logo=PhotoImage(file='logo screenshot1.png')#logo5
pic_logo1 = pic_logo.subsample(5,5)

label_piclogo=Label(root,image=pic_logo1,border=0)
label_piclogo.pack(pady=10)

centerFrame=Frame(root)
centerFrame.pack()






scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)







#text_image = Image.open('blue.png')
#text_bg_image = ImageTk.PhotoImage(text_image)





textarea=Text(centerFrame,font=('times new roman',20,'bold'),bg='grey',height=10, yscrollcommand=scrollbar.set,wrap='word')
#text_bg = textarea.image_create(text_bg_image)

textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)








questionField=Entry(root,font=('verdana',20,'bold'),bg='grey')
questionField.pack(pady=15)


#bottomframe = Frame(root,bg='green')
#bottomframe.pack()










ask_image=PhotoImage(file='circle-cropped.png')
ask_image1 = ask_image.subsample(1,1)
ask_button=Button(root,image=ask_image1,border=0,activebackground='grey',command=botReply,relief='groove')
ask_button.pack(padx=5,pady=2)









#voicepic  =  PhotoImage(file='mic.png')
#voicepic1 = voicepic.subsample(3,3)
#voice = Button(bottomframe,image=voicepic1,activebackground='black',activeforeground='red',relief='sunken')
#voice.pack(padx=5,pady=2,side=tk.LEFT)

#voice.bind('<Button-1>',audio_text)









def click(event):
    
    ask_button.invoke()




root.bind('<Return>',click)
thread = threading.Thread(target = audio_text)
thread.setDaemon(True)
thread.start()
root.mainloop()















#if __name__ == '__main__':
 #   multiprocessing.freeze_support()
    #process = multiprocessing.Process(target =audio_text)
    #process.daemon(True)
    #process.start() 
    #root.mainloop()





#if __name__ == '__main__': 
#    q = Queue()
    # Create a thread and run GUI & 
    
    
    
    
#    t1 = multiprocessing.Process(target=audio_text)
#    t1.start()
    #t2 = multiprocessing.Process(target=,args=(q,))
