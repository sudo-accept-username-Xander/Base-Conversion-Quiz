"""
Base Conversion Quiz
Zac Findlay
ver 0.03 (unfinished)
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

def Make_Hard(): # This makes the hard difficulty
    # This makes the hard mode window
    hard_window = Toplevel(root)
    hard_window.geometry("650x400")
    hard_window.title("Difficulty: Hard")
    hard_window_bg = "#f2b4b4" # Hard mode colour
    hard_window.configure(bg = hard_window_bg) 
    # Makes all of the needed buttons and labels
    sw = StopWatch(hard_window)
    sw.pack(anchor=NE)
    Button(hard_window, text="Stop", command=hard_window.destroy, height=1, width=10).pack(side=RIGHT)
    sw.MakeLabel()
    sw.tmr_lbl.config(bg=hard_window_bg)
    sw.config(bg=hard_window_bg)
    sw.Start()

def main(): # Orginal window setup makes the user choose a difficulty and welcomes the user
    easy = Button(root, text="Easy", command=Make_Easy, height=1, width=10).grid(row=1,column=0,padx=4,pady=4)
    medium = Button(root, text="Medium", command=Make_Medium, height=1, width=10).grid(row=1,column=1,padx=4,pady=4)
    hard = Button(root, text="Hard", command=Make_Hard, height=1, width=10).grid(row=1,column=2,padx=4,pady=4)
    quit_var = Button(root, text="Quit", command=root.destroy, height=1, width=10).grid(row=2,column=1,padx=4,pady=4)
    root.mainloop()

main()
