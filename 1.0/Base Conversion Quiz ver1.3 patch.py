# Imports what is needed
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from time import *
from random import randint as rand

# Sets up root
root = tk.Tk()
root.geometry("650x380")
root.title("Base Conversion Quiz")

# Initialises all of the global variables
global timer_toggle, easy_window_bg, medium_window_bg, expert_window_bg, points, answer, hex_digits, easy_button_bg, medium_button_bg, expert_button_bg
timer_toggle = True # Makes the timer class on by defult
easy_window_bg = "#d9ead3" # Easy mode colour
medium_window_bg = "#fff2cc" # Medium mode colour
expert_window_bg = "#f2b4b4" # Expert mode colour
easy_button_bg = "#b1c2ab" # Easy mode button colour
medium_button_bg = "#d7caa4" # Medium mode button colour
expert_button_bg = "#ca8c8c" # Expert mode button colour
points = 0
hex_digits = "0123456789ABCDEF" # Only these are alowed for hex

def donothing(no):
    print("Done nothing "+no)
    # This is just test code
    pass

# The folowing 2 defs are for the timer toggle code
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
    about_label = Label(about_window, text="About:\n"+                          # This is also the info of my program
                                          "Base Conversion Quiz\n"+             # Name
                                          "Zac Findlay\n"+                      # Author's name
                                          "Ver 1.3 patch\n"+                    # Ver
                                          "First ver made on 30/4/25"           # Creation date
                                          , justify=LEFT).grid(row=0, column=0)               
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
        global time_val, minutes, seconds, hseconds
        time_val = StringVar()
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set("%02d:%02d:%02d" % (minutes, seconds, hseconds))
        if hseconds <= 9 and seconds <= 9:
            time_val = str(minutes)+":0"+str(seconds)+":0"+str(hseconds)
        elif seconds <= 9:
            time_val = str(minutes)+":0"+str(seconds)+":"+str(hseconds)
        elif hseconds <= 9:
            time_val = str(minutes)+":"+str(seconds)+":0"+str(hseconds)
        else:
            time_val = str(minutes)+":"+str(seconds)+":"+str(hseconds)

    def Start(self): # Start command
        if not self._running:
            self._start = time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self): # Stop command
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
    global answer, points, easy_result_label, easy_window, load_question, question_no, easy_user_entry, easy_username_submit_button, easy_username_submited_label, easy_username_entry
    try: # This makes it so only one quiz window can be open at once (causes errors if this is alowed)
        easy_window.destroy()
        medium_window.destroy()
        expert_window.destroy()
    except:
        try:
            medium_window.destroy()
            expert_window.destroy()
        except:
            try:
                expert_window.destroy()
            except:
                pass
    easy_window = Toplevel(root)
    easy_window.geometry("650x400")
    easy_window.title("Difficulty: Easy")
    easy_window.configure(bg = easy_window_bg) 
    # Makes all of the needed buttons and labels
    stop_easy = Button(easy_window, text="Back", command=easy_window.destroy, height=1, width=10)
    stop_easy.config(bg=easy_button_bg)
    stop_easy.grid(row=1, column=4)
 
    easy_window.resizable(False, False)
    # Sets up the columns and rows
    easy_window.columnconfigure(0, minsize=110)
    easy_window.columnconfigure(1, minsize=160)
    easy_window.columnconfigure(2, minsize=125)
    easy_window.columnconfigure(3, minsize=160)
    easy_window.columnconfigure(4, minsize=110)
    easy_window.rowconfigure(0, minsize=0)
    easy_window.rowconfigure(1, minsize=0)
    easy_window.rowconfigure(2, minsize=0)
    easy_window.rowconfigure(3, minsize=50)
    easy_window.rowconfigure(4, minsize=50)
    easy_window.rowconfigure(5, minsize=50)
    easy_window.rowconfigure(6, minsize=50)
    easy_window.rowconfigure(7, minsize=50)
    easy_window.rowconfigure(8, minsize=60)
    easy_window.rowconfigure(9, minsize=0)
    
    if timer_toggle == True: # Toggle for the timer
        sw = StopWatch(easy_window)
        sw.grid(row=0, column=4)
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=easy_window_bg)
        sw.config(bg=easy_window_bg)
        sw.Start()
    else:
        easy_window.rowconfigure(2, minsize=22)
    # Sets up the labels and buttons for easy_window
    question_no = 1
    easy_question_no_label = Label(easy_window, text="Level: "+str(question_no)+"/10\nDifficulty: Easy", font=("Arial", 10), bg=easy_window_bg, justify=LEFT)
    easy_question_no_label.grid(row=9, column=0, rowspan=2)
    easy_hint_label = Label(easy_window, text="\nHint: Decimal is normal numbers.", font=("Arial", 10), bg=easy_window_bg)
    easy_hint_label.grid(row=9, column=3, columnspan=2)
    easy_question_label = Label(easy_window, font=("Arial", 11), text="", bg=easy_window_bg)
    easy_question_label.grid(row=4, column=1, columnspan=3)
    easy_user_entry = Entry(easy_window, font=("Arial", 12), width=12)
    easy_user_entry.grid(row=5, column=2)
    easy_user_entry.bind("<Return>", lambda event: check_answer(easy_user_entry, "easy"))
    easy_submit_button = Button(easy_window, text="Submit", command=lambda: check_answer(easy_user_entry, "easy"), width=10)
    easy_submit_button.config(bg=easy_button_bg)
    easy_submit_button.grid(row=6, column=2)
    easy_result_label = Label(easy_window, text="", font=("Arial", 11), bg=easy_window_bg)
    easy_result_label.grid(row=7, column=1, columnspan=3)
    easy_final_result_label = Label(easy_window, text="", font=("Arial", 11), bg=easy_window_bg)
    easy_user_entry.config(state="normal")
    easy_username_entry = Entry(easy_window, font=("Arial", 12), width=12)
    easy_username_submit_button = Button(easy_window, text="Submit username", command=lambda: chara_limit("easy", points, time_val, easy_username_entry.get().strip()))
    easy_username_submit_button.config(bg=easy_button_bg)
    easy_username_submited_label = Label(easy_window, text="", font=("Arial", 11), bg=easy_window_bg)
    
    # This is the brains of the program making all of the numbers for the user to convert.
    answer = 0
    points = 0
    def load_question():
        global question_no, answer, points, time_val
        # Resets the states of easy_user_entry
        easy_user_entry.config(state="normal")
        if question_no <= 10:
            easy_user_entry.bind("<Return>", lambda event: check_answer(easy_user_entry, "easy"))
            easy_question_no_label.config(text="Level: "+str(question_no)+"/10\nDifficulty: Easy")
        if question_no > 10: # The win state
            if timer_toggle == True:
                easy_final_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10\nTime taken:"+time_val)
                sw.Stop()
            else:
                easy_final_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10")
                time_val = "--:--:--"
            easy_submit_button.destroy()
            easy_user_entry.destroy()
            easy_question_label.destroy()
            easy_result_label.destroy()
            easy_username_entry.grid(row=6, column=2)
            easy_final_result_label.grid(row=4, column=1, columnspan=3)
            easy_username_submited_label.grid(row=7, column=1, columnspan=3)
            easy_username_submit_button.grid(row=6, column=2)
            easy_username_entry.grid(row=5, column=2)
            easy_username_entry.bind("<Return>", lambda event: chara_limit("easy", points, time_val, easy_username_entry.get().strip()))
            return
        # Generate question:
        this_to = int(rand(1,2)) # 1 is binary 2 is decimal 3 is octal 4 is hex (3+4 cant be called on easy)
        if this_to == 1: # Binary to
            this = int(rand(1,1))
            if this == 1: # Decimal
                random = rand(1,100)
                decimal_int = int(random)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                answer = decimal_int
                easy_question_label.config(text="What is "+str(binary_int)+" (Binary) in Decimal") # The output
            elif this == 2: # Octal (cant be called on easy)
                error("outside_val")
            elif this == 3: # Hex (cant be called on easy)
                error("outside_val")
            else: 
                error("outside_val")
        elif this_to == 2: # Decimal to
            this = int(rand(1,1))
            if this == 1: # Binary
                random = rand(1,100)
                decimal_int = int(random)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                answer = binary_int
                easy_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Binary") # The output
            elif this == 2: # Octal (cant be called on easy)
                error("outside_val")
            elif this == 3: # Hex (cant be called on easy)
                error("outside_val")
            else:
                error("outside_val")
        else:
            error("outside_val")

        easy_user_entry.delete(0, tk.END)
        easy_result_label.config(text="")
        question_no += 1
   
    load_question()

def Make_Medium(): # This makes the medium difficulty
    # This makes the medium mode window
    global answer, points, medium_result_label, medium_window, load_question, question_no, medium_user_entry, medium_username_submit_button, medium_username_entry, medium_username_submited_label
    try: # This makes it so only one quiz window can be open at once
        easy_window.destroy()
        medium_window.destroy()
        expert_window.destroy()
    except:
        try:
            medium_window.destroy()
            expert_window.destroy()
        except:
            try:
                expert_window.destroy()
            except:
                pass
    medium_window = Toplevel(root)
    medium_window.geometry("650x400")
    medium_window.title("Difficulty: Medium")
    medium_window.configure(bg = medium_window_bg) 
    # Makes all of the needed buttons and labels
    stop_medium = Button(medium_window, text="Back", command=medium_window.destroy, height=1, width=10)
    stop_medium.config(bg=medium_button_bg)
    stop_medium.grid(row=1, column=4)
 
    medium_window.resizable(False, False)
    # Sets up the columns and rows
    medium_window.columnconfigure(0, minsize=110)
    medium_window.columnconfigure(1, minsize=160)
    medium_window.columnconfigure(2, minsize=125)
    medium_window.columnconfigure(3, minsize=160)
    medium_window.columnconfigure(4, minsize=110)
    medium_window.rowconfigure(0, minsize=0)
    medium_window.rowconfigure(1, minsize=0)
    medium_window.rowconfigure(2, minsize=0)
    medium_window.rowconfigure(3, minsize=50)
    medium_window.rowconfigure(4, minsize=50)
    medium_window.rowconfigure(5, minsize=50)
    medium_window.rowconfigure(6, minsize=50)
    medium_window.rowconfigure(7, minsize=50)
    medium_window.rowconfigure(8, minsize=65)
    medium_window.rowconfigure(9, minsize=0)
    
    if timer_toggle == True: # Toggle for the timer
        sw = StopWatch(medium_window)
        sw.grid(row=0, column=4)
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=medium_window_bg)
        sw.config(bg=medium_window_bg)
        sw.Start()
    else:
        medium_window.rowconfigure(2, minsize=22)
    # Sets up the labels and buttons for medium_window
    question_no = 1
    medium_question_no_label = Label(medium_window, text="Level: "+str(question_no)+"/10\nDifficulty: Medium", font=("Arial", 10), bg=medium_window_bg, justify=LEFT)
    medium_question_no_label.grid(row=9, column=0, rowspan=2)
    medium_question_label = Label(medium_window, font=("Arial", 11), text="", bg=medium_window_bg)
    medium_question_label.grid(row=4, column=1, columnspan=3)
    medium_user_entry = Entry(medium_window, font=("Arial", 12), width=12)
    medium_user_entry.grid(row=5, column=2)
    medium_user_entry.bind("<Return>", lambda event: check_answer(medium_user_entry, "medium"))
    medium_submit_button = Button(medium_window, text="Submit", command=lambda: check_answer(medium_user_entry, "medium"), width=10)
    medium_submit_button.config(bg=medium_button_bg)
    medium_submit_button.grid(row=6, column=2)
    medium_result_label = Label(medium_window, text="", font=("Arial", 11), bg=medium_window_bg)
    medium_result_label.grid(row=7, column=1, columnspan=3)
    medium_final_result_label = Label(medium_window, text="", font=("Arial", 11), bg=medium_window_bg)
    medium_user_entry.config(state="normal")
    medium_username_entry = Entry(medium_window, font=("Arial", 12), width=12)
    medium_username_submit_button = Button(medium_window, text="Submit username", command=lambda: chara_limit("medium", points, time_val, medium_username_entry.get().strip()))
    medium_username_submit_button.config(bg=medium_button_bg)
    medium_username_submited_label = Label(medium_window, text="", font=("Arial", 11), bg=medium_window_bg)
    
    # This is the brains of the program making all of the numbers for the user to convert.
    answer = 0
    points = 0
    def load_question():
        global question_no, answer, points, time_val
        medium_user_entry.config(state="normal")
        if question_no <= 10:
            medium_user_entry.bind("<Return>", lambda event: check_answer(medium_user_entry, "medium"))
            medium_question_no_label.config(text="Level: "+str(question_no)+"/10\nDifficulty: Medium")
        if question_no > 10: # The win state
            if timer_toggle == True:
                medium_final_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10\nTime taken:"+time_val)
                sw.Stop()
            else:
                medium_final_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10")
                time_val = "--:--:--"
            medium_submit_button.destroy()
            medium_user_entry.destroy()
            medium_question_label.destroy()
            medium_result_label.destroy()
            medium_username_entry.grid(row=6, column=2)
            medium_final_result_label.grid(row=4, column=1, columnspan=3)
            medium_username_submited_label.grid(row=7, column=1, columnspan=3)
            medium_username_submit_button.grid(row=6, column=2)
            medium_username_entry.grid(row=5, column=2)
            medium_username_entry.bind("<Return>", lambda event: chara_limit("medium", points, time_val, medium_username_entry.get().strip()))
            return
        # Generate question:
        this_to = int(rand(1,3)) # 1 is binary 2 is decimal 3 is octal 4 is hex (4 cant be called on medium)
        if this_to == 1: # Binary to
            this = int(rand(1,2))
            if this == 1: # Decimal
                random = rand(1,100)
                decimal_int = int(random)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                answer = decimal_int
                medium_question_label.config(text="What is "+str(binary_int)+" (Binary) in Decimal") # The output
            elif this == 2: # Octal
                random = rand(1,100)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                answer = octal_int
                medium_question_label.config(text="What is "+str(binary_int)+" (Binary) in Octal") # The output
            elif this == 3: # Hex (cant be called on medium)
                error("outside_val")
            else:
                error("outside_val")
        elif this_to == 2: # Decimal to
            this = int(rand(1,2))
            if this == 1: # Binary
                random = rand(1,100)
                decimal_int = int(random)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                answer = binary_int
                medium_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Binary") # The output
            elif this == 2: # Octal
                random = rand(1,100)
                decimal_int = int(random)                
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                answer = octal_int
                medium_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Octal") # The output
            elif this == 3: # Hex (cant be called on medium)
                error("outside_val")
            else:
                error("outside_val")
        elif this_to == 3: # Octal to
            this = int(rand(1,2))
            if this == 1: # Binary
                random = rand(1,100)
                decimal_int = int(random)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                binary_int = int(binary)
                answer = binary_int
                medium_question_label.config(text="What is "+str(octal_int)+" (Octal) in Binary") # The output
            elif this == 2: # Decimal
                random = rand(1,100)
                decimal_int = int(random)                
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                answer = decimal_int
                medium_question_label.config(text="What is "+str(octal_int)+" (Octal) in Decimal") # The output
            elif this == 4: # Hex (cant be called on medium)
                error("outside_val")
            else:
                error("outside_val")
        else:
            error("outside_val")

        medium_user_entry.delete(0, tk.END)
        medium_result_label.config(text="")
        question_no += 1
   
    load_question()
    
def Make_Expert(): # This makes the expert difficulty
    # This makes the expert mode window
    global answer, points, expert_result_label, expert_window, load_question, question_no, hex_digits, expert_user_entry, expert_username_submit_button, expert_username_entry, expert_username_submited_label
    try: # This makes it so only one quiz window can be open at once
        easy_window.destroy()
        medium_window.destroy()
        expert_window.destroy()
    except:
        try:
            medium_window.destroy()
            expert_window.destroy()
        except:
            try:
                expert_window.destroy()
            except:
                pass
    expert_window = Toplevel(root)
    expert_window.geometry("650x400")
    expert_window.title("Difficulty: Expert")
    expert_window.configure(bg = expert_window_bg) 
    # Makes all of the needed buttons and labels
    stop_expert = Button(expert_window, text="Back", command=expert_window.destroy, height=1, width=10)
    stop_expert.config(bg=expert_button_bg)
    stop_expert.grid(row=1, column=4)

    expert_window.resizable(False, False)
    # Sets up the columns and rows
    expert_window.columnconfigure(0, minsize=110)
    expert_window.columnconfigure(1, minsize=160)
    expert_window.columnconfigure(2, minsize=125)
    expert_window.columnconfigure(3, minsize=160)
    expert_window.columnconfigure(4, minsize=110)
    expert_window.rowconfigure(0, minsize=0)
    expert_window.rowconfigure(1, minsize=0)
    expert_window.rowconfigure(2, minsize=0)
    expert_window.rowconfigure(3, minsize=50)
    expert_window.rowconfigure(4, minsize=50)
    expert_window.rowconfigure(5, minsize=50)
    expert_window.rowconfigure(6, minsize=50)
    expert_window.rowconfigure(7, minsize=50)
    expert_window.rowconfigure(8, minsize=65)
    expert_window.rowconfigure(9, minsize=0)
    
    if timer_toggle == True: # Toggle for the timer
        sw = StopWatch(expert_window)
        sw.grid(row=0, column=4)
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=expert_window_bg)
        sw.config(bg=expert_window_bg)
        sw.Start()
    else:
        expert_window.rowconfigure(2, minsize=22)
    # Sets up the labels and buttons for expert_window
    question_no = 1
    expert_question_no_label = Label(expert_window, text="Level: "+str(question_no)+"/10\nDifficulty: Expert", font=("Arial", 10), bg=expert_window_bg, justify=LEFT)
    expert_question_no_label.grid(row=9, column=0, rowspan=2)
    expert_question_label = Label(expert_window, font=("Arial", 11), text="", bg=expert_window_bg)
    expert_question_label.grid(row=4, column=1, columnspan=3)
    expert_user_entry = Entry(expert_window, font=("Arial", 12), width=12)
    expert_user_entry.grid(row=5, column=2)
    expert_user_entry.bind("<Return>", lambda event: check_answer(expert_user_entry, "expert"))
    expert_submit_button = Button(expert_window, text="Submit", command=lambda: check_answer(expert_user_entry, "expert"), width=10)
    expert_submit_button.config(bg=expert_button_bg)
    expert_submit_button.grid(row=6, column=2)
    expert_result_label = Label(expert_window, text="", font=("Arial", 11), bg=expert_window_bg)
    expert_result_label.grid(row=7, column=1, columnspan=3)
    expert_final_result_label = Label(expert_window, text="", font=("Arial", 11), bg=expert_window_bg)
    expert_user_entry.config(state="normal")
    expert_username_entry = Entry(expert_window, font=("Arial", 12), width=12)
    expert_username_submit_button = Button(expert_window, text="Submit username", command=lambda: chara_limit("expert", points, time_val, expert_username_entry.get().strip()))
    expert_username_submit_button.config(bg=expert_button_bg)
    expert_username_submited_label = Label(expert_window, text="", font=("Arial", 11), bg=expert_window_bg)
    
    # This is the brains of the program making all of the numbers for the user to convert.
    answer = 0
    points = 0
    def load_question():
        global question_no, answer, points, hex_digits, time_val
        expert_user_entry.config(state="normal")
        if question_no <= 10:
            expert_user_entry.bind("<Return>", lambda event: check_answer(expert_user_entry, "expert"))
            expert_question_no_label.config(text="Level: "+str(question_no)+"/10\nDifficulty: expert")
        if question_no > 10: # The win state
            if timer_toggle == True: # Timer on stuff
                expert_final_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10\nTime taken:"+time_val)
                sw.Stop()
            else: # Timer off stuff
                expert_final_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10")
                time_val = "--:--:--"
            expert_submit_button.destroy()
            expert_user_entry.destroy()
            expert_question_label.destroy()
            expert_result_label.destroy()
            expert_username_entry.grid(row=6, column=2)
            expert_final_result_label.grid(row=4, column=1, columnspan=3)
            expert_username_submited_label.grid(row=7, column=1, columnspan=3)
            expert_username_submit_button.grid(row=6, column=2)
            expert_username_entry.grid(row=5, column=2)
            expert_username_entry.bind("<Return>", lambda event: chara_limit("expert", points, time_val, expert_username_entry.get().strip()))
            return
        # Generate question:
        this_to = int(rand(1,4)) # 1 is binary 2 is decimal 3 is octal 4 is hex
        if this_to == 1: # Binary to
            this = int(rand(1,3))
            if this == 1: # Decimal
                random = rand(1,100)
                decimal_int = int(random)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                answer = decimal_int
                expert_question_label.config(text="What is "+str(binary_int)+" (Binary) in Decimal") # The output
            elif this == 2: # Octal
                random = rand(1,100)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                answer = octal_int
                expert_question_label.config(text="What is "+str(binary_int)+" (Binary) in Octal") # The output
            elif this == 3: # Hex
                random = rand(1,100)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                divider = random
                hex_str = ""
                while divider > 0:
                    remainder = divider % 16
                    hex_digit = hex_digits[remainder]
                    hex_str = hex_digit + hex_str
                    divider = divider // 16
                answer = hex_str
                expert_question_label.config(text="What is "+str(binary_int)+" (binary) in Hex") # The output
            else:
                error("outside_val")
        elif this_to == 2: # Decimal to
            this = int(rand(1,1))
            if this == 1: # Binary
                random = rand(1,100)
                decimal_int = int(random)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                answer = binary_int
                expert_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Binary") # The output
            elif this == 2: # Octal
                random = rand(1,100)
                decimal_int = int(random)
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                answer = octal_int
                expert_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Octal") # The output
            elif this == 3: # Hex
                random = rand(1,100)
                decimal_int = int(random)
                divider = random
                hex_str = ""
                while divider > 0:
                    remainder = divider % 16
                    hex_digit = hex_digits[remainder]
                    hex_str = hex_digit + hex_str
                    divider = divider // 16
                answer = hex_str
                expert_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Hex") # The output
            else:
                error("outside_val")
        elif this_to == 3: # Octal to
            this = int(rand(1,3))
            if this == 1: # Binary
                random = rand(1,100)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                answer = binary_int
                expert_question_label.config(text="What is "+str(octal_int)+" (Octal) in Binary") # The output
            elif this == 2: # Decimal
                random = rand(1,100)
                decimal_int = int(random)                
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                answer = decimal_int
                expert_question_label.config(text="What is "+str(octal_int)+" (Octal) in Decimal") # The output
            elif this == 3: # Hex
                random = rand(1,100)
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                divider = random
                hex_str = ""
                while divider > 0:
                    remainder = divider % 16
                    hex_digit = hex_digits[remainder]
                    hex_str = hex_digit + hex_str
                    divider = divider // 16
                answer = hex_str
                expert_question_label.config(text="What is "+str(octal_int)+" (Octal) in Hex") # The output
            else:
                error("outside_val")
        elif this_to == 4: # Hex to
            this = int(rand(1,3))
            if this == 1: # Binary
                random = rand(1,100)
                devider = random
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
                binary_int = int(binary)
                divider = random
                hex_str = ""
                while divider > 0:
                    remainder = divider % 16
                    hex_digit = hex_digits[remainder]
                    hex_str = hex_digit + hex_str
                    divider = divider // 16
                answer = binary_int
                expert_question_label.config(text="What is "+str(hex_str)+" (Hex) in binary") # The output
            elif this == 2: # Decimal
                random = rand(1,100)
                decimal_int = int(random)
                divider = random
                hex_str = ""
                while divider > 0:
                    remainder = divider % 16
                    hex_digit = hex_digits[remainder]
                    hex_str = hex_digit + hex_str
                    divider = divider // 16
                answer = decimal_int
                expert_question_label.config(text="What is "+str(hex_str)+" (Hex) in Decimal") # The output
            elif this == 3: # Octal
                random = rand(1,100)
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                divider = random
                hex_str = ""
                while divider > 0:
                    remainder = divider % 16
                    hex_digit = hex_digits[remainder]
                    hex_str = hex_digit + hex_str
                    divider = divider // 16
                answer = octal_int
                expert_question_label.config(text="What is "+str(hex_str)+" (Hex) in Octal") # The output
            else:
                error("outside_val")
        else:
            error("outside_val")

        expert_user_entry.delete(0, tk.END)
        expert_result_label.config(text="")
        question_no += 1
   
    load_question()
    
def check_answer(entry, difficulty, event=None): # This is the answer checker
    global answer, points, easy_result_label, easy_window, easy_user_entry, medium_window, medium_result_label, medium_user_entry, expert_window, expert_result_label, expert_user_entry, load_question
    if difficulty == "easy": # This is the answer checker for easy
        user_input = entry.get().strip()
        if not user_input.isdigit():
            messagebox.showerror("Error", "Answer must be a whole non-negative number.")
            return
        if int(user_input) == answer:
            points += 1
            easy_result_label.config(text="Correct!")
            easy_user_entry.config(state="disabled")
            easy_user_entry.unbind("<Return>")

        else:
            easy_result_label.config(text="Incorrect.\nThe correct answer was "+str(answer))
            easy_user_entry.config(state="disabled")
            easy_user_entry.unbind("<Return>")

        easy_window.after(1500, load_question)
        return entry.delete(0, tk.END)
    elif difficulty == "medium": # This is the answer checker for medium
        user_input = entry.get().strip()
        if not user_input.isdigit():
            messagebox.showerror("Error", "Answer must be a whole non-negative number.")
            return
        if int(user_input) == answer:
            points += 1
            medium_result_label.config(text="Correct!")
            medium_user_entry.config(state="disabled")
            medium_user_entry.unbind("<Return>")

        else:
            medium_result_label.config(text="Incorrect.\nThe correct answer was "+str(answer))
            medium_user_entry.config(state="disabled")
            medium_user_entry.unbind("<Return>")

        medium_window.after(1500, load_question)
        return entry.delete(0, tk.END)
    elif difficulty == "expert": # This is the answer checker for expert
        user_input = entry.get().strip().upper() # Because hex uses letters I have to make expert allow some letters
        if user_input in hex_digits:
            if str(user_input) == str(answer):
                points += 1
                expert_result_label.config(text="Correct!")
                expert_user_entry.config(state="disabled")
                expert_user_entry.unbind("<Return>")
            else:
                expert_result_label.config(text="Incorrect.\nThe correct answer was "+str(answer))
                expert_user_entry.config(state="disabled")
                expert_user_entry.unbind("<Return>")

            expert_window.after(1500, load_question)
            return entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Answer must be a whole non-negative number\nor letters used in hex.")

def write_score(difficulty, score, time_taken, user): # Writes the score into a file named "Score.txt" with difficulty, the username, score ot of 10, and the time the user took
    global easy_username_submit_button, medium_window, expert_window
    if difficulty == "easy": # This is the place the user can input a username
        easy_username_submit_button.config(state="disabled")
        easy_username_submited_label.config(text="Username submited")
        easy_username_entry.unbind("<Return>")
    elif difficulty == "medium":
        medium_username_submit_button.config(state="disabled")
        medium_username_submited_label.config(text="Username submited")
        medium_username_entry.unbind("<Return>")
    elif difficulty == "expert":
        expert_username_submit_button.config(state="disabled")
        expert_username_submited_label.config(text="Username submited")
        expert_username_entry.unbind("<Return>")
    with open("Score.txt", "a") as file: # Writes the difficulty, username, score, then time (or --:--:-- for no time) to a file
        file.write(f"{difficulty},{user},{score},{time_taken}\n")

def score_func(difficulty): # This is for the user to check old scores and compare them to other users, times, or scores
    score_window = Toplevel(root)
    score_window.geometry("650x400")
    score_window.title("Scores For "+difficulty.capitalize())

    score_window.resizable(False, False)

    score_window.rowconfigure(0, minsize=25)
    score_window.rowconfigure(1, minsize=50)
    score_window.rowconfigure(2, minsize=0)
    score_window.rowconfigure(3, minsize=0)
    score_window.rowconfigure(4, minsize=0)
    score_window.rowconfigure(5, minsize=0)
    score_window.rowconfigure(6, minsize=0)
    score_window.rowconfigure(7, minsize=0)
    score_window.rowconfigure(8, minsize=0)
    score_window.rowconfigure(9, minsize=0)
    score_window.rowconfigure(10, minsize=0)
    score_window.rowconfigure(11, minsize=0)
    
    score_window.columnconfigure(0, minsize=25)
    score_window.columnconfigure(1, minsize=0)
    score_window.columnconfigure(2, minsize=0)
    score_window.columnconfigure(3, minsize=0)
    score_window.columnconfigure(4, minsize=0)

    score_window_name = Label(score_window, font=("arial", 20), text="Scores For "+difficulty.capitalize(), width=16).grid(row=1, column=2, columnspan=3) # Window name
    score_window_frame = Frame(score_window, height=300, width=600, bg="#FFFFFF").grid(row=2, rowspan=10, column=2, columnspan=3) # Frame for the info from the file
    row_no = 0
    score_val = 10

    try:
        with open("Score.txt", "r") as file: # Opens file
            records = file.readlines() # Reads file
            filtered = []
            for record in records:
                try:
                    diffi, user, score, time_taken = record.strip().split(",")
                    if diffi.strip().lower() == difficulty.lower():
                        time_sorter = time_taken
                        if "--" in time_sorter:
                            time_sorter = "99:99:99"
                        filtered.append((int(score), time_sorter, user.strip(), score, time_taken))
                except:
                    continue

            # Sort by score then fastest time (note scores that do not have a time eg "--:--:--" are last)
            score_sorted = sorted(filtered, key=lambda x: (-x[0], x[1]))[:10]

            if score_sorted:
                for row_no, (_, _, user, score, time_taken) in enumerate(score_sorted):
                    Label(score_window, text=user, justify=LEFT, bg="#FFFFFF").grid(row=2 + row_no, column=2)
                    Label(score_window, text=str(score)+"/10", justify=LEFT, bg="#FFFFFF").grid(row=2 + row_no, column=3)
                    Label(score_window, text=time_taken, justify=LEFT, bg="#FFFFFF").grid(row=2 + row_no, column=4)
            else: # No scores in choesn difficulty
                Label(score_window, text="No scores for this difficulty.\nMaybe you can be the first?", bg="#FFFFFF").grid(row=3, column=2, columnspan=3)

    except FileNotFoundError: # No file found
        with open("Score.txt", "a") as file:
            pass
        Label(score_window, text="No scores for this difficulty.\nMaybe you can be the first?", bg="#FFFFFF").grid(row=3, column=2, columnspan=3)
                    
def chara_limit(difficulty, score, time_taken, entry):
    if len(entry) > 14:
        return messagebox.showerror("Error", "Cannot have a username longer than 15 characters")
    elif len(entry) == 0 or len(entry) == 1:
        return messagebox.showerror("Error", "Cannot have a username shorter than 2 characters")
    else:
        return write_score(difficulty, score, time_taken, entry)
    
def back_to_root():
    global quit_window, quit_window_open
    quit_window_open = False
    quit_window.destroy()

def really_quit(): # Askes the user if they really want to quit (this is not called on file->exit)
    global quit_window, quit_window_open
    if quit_window_open == False:
        quit_window_open = True
        quit_window = Toplevel(root)
        quit_window.geometry("250x50")
        quit_window.title("Really Quit?")
        really_quit_label = Label(quit_window, text="Do You Really Want To Quit?", width=25).grid(row=0, column=1, columnspan=3)
        yes_button = Button(quit_window, text="Yes", command=root.destroy, width=10, bg=expert_window_bg).grid(row=1, column=1) # Closes the window
        # Makes it so only one really_quit windows can be active by calling a fuction that makes it kill the window and make quit_window_open = False
        no_button = Button(quit_window, text="No", command=back_to_root, width=10, bg=easy_window_bg).grid(row=1, column=3)
        quit_window.columnconfigure(0, minsize=35)
        quit_window.columnconfigure(1, minsize=10)
        quit_window.columnconfigure(2, minsize=20)
        quit_window.columnconfigure(3, minsize=10)
        quit_window.columnconfigure(4, minsize=35)
        quit_window.resizable(False, False)
    
def main(): # Root window setup makes the user choose a difficulty and welcomes the user
    global quit_window_open
    root.rowconfigure(0, minsize=0)
    root.rowconfigure(1, minsize=150)
    root.rowconfigure(2, minsize=50)
    root.rowconfigure(3, minsize=0)
    root.rowconfigure(4, minsize=0)
    root.rowconfigure(5, minsize=0)
    root.columnconfigure(0, minsize=0)
    root.columnconfigure(1, minsize=0)
    root.columnconfigure(2, minsize=0)
    root.columnconfigure(3, minsize=0)
    root.columnconfigure(4, minsize=0)
    
    root.configure(bg="#FFFFFF")
    root.resizable(False, False)
    # Makes all the buttons, labels and frames
    frame = Frame(root, width=650,height=80, bg="#FFFFFF").grid(row=3, column=0, columnspan=5) # Frame for the name
    frame1 = Frame(root, bg="#FFFFFF", width=630,height=80).grid(padx=10, pady=10, row=4, column=0, columnspan=5, rowspan=2) # Frame for the buttons
    easy = Button(frame1, text="Easy", command=Make_Easy, width=10, bg=easy_window_bg).grid(padx=4, pady=8, row=4, column=0) # Easy
    medium = Button(frame1, text="Medium", command=Make_Medium, width=10, bg=medium_window_bg).grid(padx=4, pady=8, row=4, column=2) # Medium
    expert = Button(frame1, text="Expert", command=Make_Expert, width=10, bg=expert_window_bg).grid(padx=4, pady=8, row=4, column=4) # Expert
    quit_var = Button(frame1, text="Quit", command=really_quit, width=10).grid(padx=4, pady=8, row=5, column=2) # Exit
    name_label = Label(frame, font=("impact", 32), text="Base Conversion\nQuiz", width=16).grid(row=1, column=1, columnspan=3) # The name of the program
    choose_difficulty_label = Label(root, font=("arial", 14), text="Choose Your Difficulty", bg="#FFFFFF").grid(row=2, column=0, columnspan=5)
    easy_label = Label(frame, bg="#FFFFFF", font=("",9), text="Easy is decimal to binary\n and binary to decimal.", fg="#38761d").grid(row=3, column=0) # Difficulty Context
    medium_label = Label(frame, bg="#FFFFFF", font=("",9), text="Medium is octal to decimal and binary\n and decimal to octal and binary.", fg="#b45f06").grid(row=3, column=2) # Difficulty Context
    expert_label = Label(frame, bg="#FFFFFF", font=("",9), text="Expert is decimal to all so\n far and also hex and back.", fg="#dc0000").grid(row=3, column=4) # Difficulty Context

    quit_window_open = False
    
    menubar = Menu(root) # Menu bar
    file_menu = Menu(menubar, tearoff=0) # Settup the main dropdowns
    settings_menu = Menu(menubar, tearoff=0)
    timer_settings = Menu(settings_menu, tearoff=0)
    score_menu = Menu(menubar, tearoff=0)
    help_menu = Menu(menubar, tearoff=0)
    
    menubar.add_cascade(label="File", menu=file_menu) # File
    file_menu.add_command(label="Exit", command=root.destroy)
    
    menubar.add_cascade(label="Settings", menu=settings_menu) # Settings
    settings_menu.add_cascade(label="Timer", menu=timer_settings) # Adds timer on/off
    timer_settings.add_radiobutton(label="Enabled", command=timer_on) # Timer on
    timer_settings.add_radiobutton(label="Disabled", command=timer_off) # Timer off

    score_menu.add_command(label="Show easy score", command=lambda:score_func("easy"))
    score_menu.add_command(label="Show medium score", command=lambda:score_func("medium"))
    score_menu.add_command(label="Show expert score", command=lambda:score_func("expert"))
    menubar.add_cascade(label="Score", menu=score_menu)
    
    menubar.add_cascade(label="Help", menu=help_menu)    
    help_menu.add_command(label="About...", command=about) # About...

    root.config(menu=menubar)
    
    root.mainloop()
    
main()
