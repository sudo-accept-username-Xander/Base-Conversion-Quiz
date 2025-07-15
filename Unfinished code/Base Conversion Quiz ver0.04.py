"""
Base Conversion Quiz
Zac Findlay
ver 0.04 (unfinished)
30/4/25
"""
# Imports what is needed
from tkinter import *
import tkinter as tk
import time

# Sets up root
root = tk.Tk()
root.geometry("650x400")
root.title("Base Conversion Quiz")

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
        self.tmr_lbl.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self): # This updates the label
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap): # This is the underlying math that _update takes from
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set("%02d:%02d:%02d" % (minutes, seconds, hseconds))

    def Start(self): # Start command
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self): # Stop command
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self): # Reset command
        self._start = time.time()
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
    sw = StopWatch(easy_window)
    sw.pack(anchor=NE)
    Button(easy_window, text="Stop", command=easy_window.destroy, height=1, width=10).pack(side=RIGHT)
    sw.MakeLabel()
    sw.tmr_lbl.config(bg=easy_window_bg)
    sw.config(bg=easy_window_bg)
    sw.Start()

def Make_Medium(): # This makes the medium difficulty
    # This makes the medium mode window
    medium_window = Toplevel(root)
    medium_window.geometry("650x400")
    medium_window.title("Difficulty: Medium")
    medium_window_bg = "#fff2cc" # Medium mode colour
    medium_window.configure(bg = medium_window_bg) 
    # Makes all of the needed buttons and labels
    sw = StopWatch(medium_window)
    sw.pack(anchor=NE)
    Button(medium_window, text="Stop", command=medium_window.destroy, height=1, width=10).pack(side=RIGHT)
    sw.MakeLabel()
    sw.tmr_lbl.config(bg=medium_window_bg)
    sw.config(bg=medium_window_bg)
    sw.Start()

def Make_Expert(): # This makes the expert difficulty
    # This makes the expert mode window
    expert_window = Toplevel(root)
    expert_window.geometry("650x400")
    expert_window.title("Difficulty: Expert")
    expert_window_bg = "#f2b4b4" # Expert mode colour
    expert_window.configure(bg = expert_window_bg) 
    # Makes all of the needed buttons and labels
    sw = StopWatch(expert_window)
    sw.pack(anchor=NE)
    Button(expert_window, text="Stop", command=expert_window.destroy, height=1, width=10).pack(side=RIGHT)
    sw.MakeLabel()
    sw.tmr_lbl.config(bg=expert_window_bg)
    sw.config(bg=expert_window_bg)
    sw.Start()

def main(): # Orginal window setup makes the user choose a difficulty and welcomes the user
    root.rowconfigure(0, minsize=100)
    root.rowconfigure(1, minsize=0)
    root.rowconfigure(2, minsize=100)
    root.rowconfigure(3, minsize=0)
    root.columnconfigure(0, minsize=0)
    root.columnconfigure(1, minsize=0)
    root.columnconfigure(2, minsize=0)
    root.columnconfigure(3, minsize=0)
    root.columnconfigure(4, minsize=0)
    root.configure(bg="#FFFFFF")
    frame = Frame(root, width=250,height=80).grid(padx=10, pady=10, row=1, column=1, columnspan=3)
    frame1 = Frame(root, bg="#FFFFFF", width=630,height=80).grid(padx=10, pady=10, row=4, column=0, columnspan=5, rowspan=2)
    easy = Button(frame1, text="Easy", command=Make_Easy, width=10).grid(padx=4, pady=8, row=4, column=0) 
    medium = Button(frame1, text="Medium", command=Make_Medium, width=10).grid(padx=4, pady=8, row=4, column=2) 
    expert = Button(frame1, text="Expert", command=Make_Expert, width=10).grid(padx=4, pady=8, row=4, column=4) 
    quit_var = Button(frame1, text="Quit", command=root.destroy, width=10).grid(padx=4, pady=8, row=5, column=2)
    menubar = menubar(root)
    root.mainloop()

main()
