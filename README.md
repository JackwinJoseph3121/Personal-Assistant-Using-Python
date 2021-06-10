# Personal Assistant  for Desktop using Python

The name of this personal assistant is Thursday.

This is a personal assistant made using python.It is a program packed with many functions like playing a song, taking a picture, taking a screenhot to name a few. It gives a personalised experience for the user to tkinker with. The nlp used with the chatterbot module makes it a smart personal assistant.It has functions like getting the path of a file or application when the application is specified.It has the text to speech and speech to text conversion to make the program more user friendly and interesting.The functions of this personal assistant are as follows:



*  Screenshot the pc with the timestamp: **Command**- "take screenshot" or "Take screenshot".
* Playing songs from the desired file location.**Command**- "Play song" or "play song".
*  Opening links in the webbrowser. **Command**-"open website 'desired website'" or "Open website 'desired website'".
* Opening files and desktop application using the program. **Command**-"Open application (desired application or file)" or "Open application (desired application or file)".Desired applications like spotify,notepad,etc.
* Text to speech and speech to text conversion to interact with  the program.Just press the button and ask.
* Taking a picture and saving it in the desire location.**Command**- "Take pic" or "take pic" or "Take picture".
* Giving the current date and time when asked .**Command**-"Date and time" or "date today".
* Giving the file path when the asked for the path.**Command**-"Give path" or "give path"(not working at the moment)






The dependancies and the required modules are as follows:



* **Chatterbot**- required for the chatbot features of the personal assisant.
* **speech recognition(google)**- required for speech to text conversion.
* **Tkinter**- for the graphical use interface of the application.
* **Threading** - used for the parallel tasks happening in the application.
* **os** - used for file and the desktop system operations.
* **OpenCv** - used for taking pictures when the command is invoked.
* **pyttsx3** - used for the text to speech conversion.
* **webbrowser** - used for opening links on the browser when function is invoked.
* **Pillow** - used for working with image files in the program.
* **pyscreenshot** - used for grabbing the screenshot when the function is invoked.
* **playsound** - It is used for playing the song when the function is invoked.
* **datetime** - used for getting the date and time of system.

All the modules can be install using pip. There might be problem only in installing the speech recognition module as there are some dependencies like pyaudio for it.



pip install speech recognition

for pyaudio installation-  

                          pip install pipwin
                          pipwin install pyaudio


for chatterbot installation_ 

                               pip install Chatterbot

                             pip install spacy==2.3.3(dependancy of the chatterbot module)
                             
                             run cmd as administrator
                             
                             run- python -m spacy download en(this should be done in the directory of lib/sites and packages in python)


This works well for python 3.7 . Not sure if it would work for other versions.There is only one yaml folder for chatbot corpusle training. You can get it from gunthercox chat corplusles.Try it and let me know.
