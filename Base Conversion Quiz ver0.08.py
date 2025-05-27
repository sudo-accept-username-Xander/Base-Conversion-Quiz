# Imports what is needed
from tkinter import *
import tkinter as tk
from time import *

# Sets up root
root = tk.Tk()
root.geometry("650x400")
root.title("Base Conversion Quiz")

# Makes the timer class on by defult
global timer_toggle 
timer_toggle = True

def donothing():
    print("Done nothing")
    # This is just test code
    pass

def timer_on():
    global timer_toggle
    if timer_toggle == True:
        pass
    elif timer_toggle == False:
        timer_toggle = True

def timer_off():
    global timer_toggle
    if timer_toggle == False:
        pass
    elif timer_toggle == True:
        timer_toggle = False

def about(): # Makes the About window
    about_window = Toplevel(root)
    about_window.geometry("250x100")
    about_window.title("About")
    about_window.columnconfigure(0, minsize=150)
    about_label = Label(about_window,text="About:\n"+                           # This is also the info of my program
                                          "Base Conversion Quiz\n"+             # Name
                                          "Zac Findlay\n"+                      # Author's name
                                          "ver 0.08 (unfinished)\n"+            # Ver
                                          "30/4/25"                             # Creation date
                                          ).grid(row=0, column=0)               
    quit_var = Button(about_window, text="Back", command=about_window.destroy, width=10).grid(row=0, column=1)
    about_window.resizable(False, False)

class StopWatch(Frame): # This sets up the timer for all difficulties
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()

    def MakeLabel(self): # This makes the label that it effects
        self.tmr_lbl = tk.Label(self, textvariable=self.timestr, height=1, width=10, font=("arial", 10, "bold"))
        self._setTime(self._elapsedtime)
        self.tmr_lbl.grid()

    def _update(self): # This updates the label
        self._elapsedtime = time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap): # This is the underlying math that _update takes from
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set("%02d:%02d:%02d" % (minutes, seconds, hseconds))

    def Start(self): # Start command
        if not self._running:
            self._start = time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self): # Stop command (not needed as yet)
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self): # Reset command (not needed as yet)
        self._start = time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

def Make_Easy(): # This makes the easy difficulty
    # This makes the easy mode window
    easy_window = Toplevel(root)
    easy_window.geometry("650x400")
    easy_window.title("Difficulty: Easy")
    easy_window_bg = "#d9ead3" # Easy mode colour
    easy_window.configure(bg = easy_window_bg) 
    # Makes all of the needed buttons and labels
    stop_easy = Button(easy_window, text="Stop", command=easy_window.destroy, height=1, width=10)
    stop_easy.config(bg="#b1c2ab")
    stop_easy.grid(row=1, column=4)
    if timer_toggle == True:
        sw = StopWatch(easy_window)
        sw.grid(row=0, column=4)
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=easy_window_bg)
        sw.config(bg=easy_window_bg)
        sw.Start()
    
    easy_window.resizable(False, False)
    
    easy_window.columnconfigure(0, minsize=110)
    easy_window.columnconfigure(1, minsize=165)
    easy_window.columnconfigure(2, minsize=115)
    easy_window.columnconfigure(3, minsize=165)
    easy_window.columnconfigure(4, minsize=110)



def Make_Medium(): # This makes the medium difficulty
    # This makes the medium mode window
    medium_window = Toplevel(root)
    medium_window.geometry("650x400")
    medium_window.title("Difficulty: Medium")
    medium_window_bg = "#fff2cc" # Medium mode colour
    medium_window.configure(bg = medium_window_bg) 
    # Makes all of the needed buttons and labels
    stop_medium = Button(medium_window, text="Stop", command=medium_window.destroy, height=1, width=10)
    stop_medium.config(bg="#d7caa4")
    stop_medium.grid(row=1, column=4)
    if timer_toggle == True:
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=medium_window_bg)
        sw.config(bg=medium_window_bg)
        sw = StopWatch(medium_window)
        sw.grid(row=0, column=4)
        sw.Start()
    
    medium_window.resizable(False, False)
    
    medium_window.columnconfigure(0, minsize=110)
    medium_window.columnconfigure(1, minsize=165)
    medium_window.columnconfigure(2, minsize=115)
    medium_window.columnconfigure(3, minsize=165)
    medium_window.columnconfigure(4, minsize=110)

def Make_Expert(): # This makes the expert difficulty
    # This makes the expert mode window
    expert_window = Toplevel(root)
    expert_window.geometry("650x400")
    expert_window.title("Difficulty: Expert")
    expert_window_bg = "#f2b4b4" # Expert mode colour
    expert_window.configure(bg = expert_window_bg) 
    # Makes all of the needed buttons and labels
    stop_expert = Button(expert_window, text="Back", command=expert_window.destroy, height=1, width=10)
    stop_expert.config(bg="#ca8c8c")
    stop_expert.grid(row=1, column=4)
    if timer_toggle == True:
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=expert_window_bg)
        sw.config(bg=expert_window_bg)
        sw = StopWatch(expert_window)
        sw.grid(row=0, column=4)
        sw.Start()

    expert_window.resizable(False, False)
    
    expert_window.columnconfigure(0, minsize=110)
    expert_window.columnconfigure(1, minsize=165)
    expert_window.columnconfigure(2, minsize=115)
    expert_window.columnconfigure(3, minsize=165)
    expert_window.columnconfigure(4, minsize=110)
    
def main(): # Root window setup makes the user choose a difficulty and welcomes the user
    root.rowconfigure(0, minsize=50)
    root.rowconfigure(1, minsize=0)
    root.rowconfigure(2, minsize=60)
    root.rowconfigure(3, minsize=0)
    root.rowconfigure(4, minsize=0)
    root.rowconfigure(5, minsize=0)
    root.columnconfigure(0, minsize=100)
    root.columnconfigure(1, minsize=0)
    root.columnconfigure(2, minsize=0)
    root.columnconfigure(3, minsize=0)
    root.columnconfigure(4, minsize=100)
    
    root.configure(bg="#FFFFFF")
    root.resizable(False, False)
    # Makes all the buttons, labels and frames
    frame = Frame(root, width=650,height=80).grid(row=3, column=0, columnspan=5)
    frame1 = Frame(root, bg="#FFFFFF", width=630,height=80).grid(padx=10, pady=10, row=4, column=0, columnspan=5, rowspan=2)
    easy = Button(frame1, text="Easy", command=Make_Easy, width=10).grid(padx=4, pady=8, row=4, column=0) 
    medium = Button(frame1, text="Medium", command=Make_Medium, width=10).grid(padx=4, pady=8, row=4, column=2) 
    expert = Button(frame1, text="Expert", command=Make_Expert, width=10).grid(padx=4, pady=8, row=4, column=4) 
    quit_var = Button(frame1, text="Quit", command=root.destroy, width=10).grid(padx=4, pady=8, row=5, column=2)
    name_label = Label(frame, font=("impact", 32), text="Base Conversion\nQuiz").grid(row=1, column=1, columnspan=3)
    
    menubar = Menu(root) # Menu bar
    file_menu = Menu(menubar, tearoff=0)
    settings_menu = Menu(menubar, tearoff=0)
    timer_settings = Menu(settings_menu, tearoff=0)
    help_menu = Menu(menubar, tearoff=0)
    
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)
    timer_settings.add_radiobutton(label="Enabled", command=timer_on)
    timer_settings.add_radiobutton(label="Disabled", command=timer_off)
    

    settings_menu.add_cascade(label="Timer", menu=timer_settings) #add timer on/off

    menubar.add_cascade(label="Settings", menu=settings_menu)
    root.config(menu=menubar)
    
    
   
    help_menu.add_command(label="About...", command=about)
    menubar.add_cascade(label="Help", menu=help_menu)
    root.config(menu=menubar)

    root.mainloop()

main()
