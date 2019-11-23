import threading

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as filedialog
from tkinter import StringVar
from tkinter import IntVar
from tkinter import RAISED
import os

from spleeter.separator import Separator
from spleeter.utils.audio.adapter import get_default_audio_adapter

import subprocess
import threading


def selectFile():
    myText.set(filedialog.askopenfilename())
    return 

def selectDir():
    myDir.set(filedialog.askdirectory())
    return 


def separateAudio():
    if myText.get() and myDir.get():
        stems = ''
        if var.get() == 1:
            stems = '2Stems.json'
        elif var.get() == 2:
            stems = '4Stems.json'
        elif var.get() == 3:
            stems = '5Stems.json'

        DoSeparstion(stems)
    else:
        tk.messagebox.showinfo(
            message="You must select a file and a Final Directory to proceed", title="Warning!")


def DoSeparstion(stems):
    loadingState(True)
    try:
        separator = Separator(stems)
        separator.separate_to_file(myText.get(), myDir.get(), synchronous=False)
        if tk.messagebox.askyesno(message="Process completed, open result folder?", title="Success!"):
            subprocess.Popen(f'explorer {os.path.realpath(myDir.get())}')
    except Exception as identifier:
        tk.messagebox.showinfo(message="Error: "+identifier, title="Error")

    loadingState(False)
    return


def runMyThread():
    x = threading.Thread(target=separateAudio)
    x.daemon = True
    x.start()


def loadingState(state):
    if state:
        myLoading.set('Processing please wait...')
        btnSeparate['state'] = 'disabled'
        btnFile['state'] = 'disabled'
        btnDir['state'] = 'disabled'
        rb2Stems['state'] = 'disabled'
        rb4Stems['state'] = 'disabled'
        rb5Stems['state'] = 'disabled'
    else:
        myLoading.set('')
        btnSeparate['state'] = 'normal'
        btnFile['state'] = 'normal'
        btnDir['state'] = 'normal'
        rb2Stems['state'] = 'normal'
        rb4Stems['state'] = 'normal'
        rb5Stems['state'] = 'normal'


if __name__ == "__main__":

    global x

    # GUI Base
    global root
    root = tk.Tk()
    root.title('Spleeter Box')
    root.minsize(600, 600)

    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2) - 100
    positionDown = int(root.winfo_screenheight() /2 - windowHeight/2) - 250

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    canvas = tk.Canvas(root, height=600, width=600, bg='#263D42')
    canvas.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white")
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(6, weight=1)
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # widgets

    myPady = 10

    global myText
    global myDir

    myTextDesc = StringVar()
    myText = StringVar()
    myDirDesc = StringVar()
    myDir = StringVar()

    global myLoading
    myLoading = StringVar()
    lblLoading = tk.Label(root, textvariable=myLoading)
    lblLoading.pack(anchor=tk.W)


    # File
    myTextDesc.set('File:')

    lblFileDesc = tk.Label(frame, textvariable=myTextDesc)
    lblFileDesc.grid(column=0, row=0, pady=myPady)

    lblFile = tk.Label(frame, textvariable=myText)
    lblFile.grid(column=0, row=1, pady=myPady)

    global btnFile
    btnFile = tk.Button(frame, text="Select File", command=selectFile)
    btnFile.grid(column=0, row=2, pady=myPady)

    # Directory
    myDirDesc.set('Directory:')

    lblDirDesc = tk.Label(frame, textvariable=myDirDesc)
    lblDirDesc.grid(column=0, row=3, pady=myPady)

    lblDir = tk.Label(frame, textvariable=myDir)
    lblDir.grid(column=0, row=4, pady=myPady)

    global btnDir
    btnDir = tk.Button(frame, text="Select Dir", command=selectDir)

    btnDir.grid(column=0, row=5, pady=myPady)

    # radioButtons
    var = IntVar()
    var.set(1)  # Set option 1 as default

    global rb2Stems
    rb2Stems = tk.Radiobutton(root, text="Vocals/accompaniment", variable=var, value=1)
    rb2Stems.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.55)


    global rb4Stems
    rb4Stems = tk.Radiobutton(root, text="Vocals/drums/bass/other", variable=var, value=2)
    rb4Stems.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.65)


    global rb5Stems
    rb5Stems = tk.Radiobutton(root, text="Vocals/drums/bass/piano/other", variable=var, value=3)
    rb5Stems.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.75)

    global btnSeparate
    btnSeparate = tk.Button(root, text="Separate Audio", command=runMyThread)
    btnSeparate.place(relwidth=0.15, relx=0.425, rely=0.93)


    root.mainloop()


