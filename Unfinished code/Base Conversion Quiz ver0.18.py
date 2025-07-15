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

# Makes the timer class on by defult
global timer_toggle, easy_window_bg, medium_window_bg, expert_window_bg, points, answer
timer_toggle = True
easy_window_bg = "#d9ead3" # Easy mode colour
medium_window_bg = "#fff2cc" # Medium mode colour
expert_window_bg = "#f2b4b4" # Expert mode colour
points = 0

def error(error_val):
    error_window = Toplevel(root)
    error_window.geometry("250x100")
    error_window.title("Error window")
    if error_val == "outside_val":
        error_label = Label(error_window, text="Error: outside_val").grid()
    else:
        error_label = Label(error_window, text="Error: UNDEFINED ERROR").grid()

def donothing(no):
    print("Done nothing"+no)
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
                                          "ver 0.18 (unfinished)\n"+            # Ver
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
    global answer, points, easy_result_label, easy_window, load_question, question_no, easy_user_entry
    easy_window = Toplevel(root)
    easy_window.geometry("650x400")
    easy_window.title("Difficulty: Easy")
    easy_window.configure(bg = easy_window_bg) 
    # Makes all of the needed buttons and labels
    stop_easy = Button(easy_window, text="Back", command=easy_window.destroy, height=1, width=10)
    stop_easy.config(bg="#b1c2ab")
    stop_easy.grid(row=1, column=4)
 
    easy_window.resizable(False, False)
    
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
    
    if timer_toggle == True:
        sw = StopWatch(easy_window)
        sw.grid(row=0, column=4)
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=easy_window_bg)
        sw.config(bg=easy_window_bg)
        sw.Start()
    else:
        easy_window.rowconfigure(2, minsize=22)

    question_no = 1
    easy_question_no_label = Label(easy_window, text="Level: "+str(question_no)+"/10\nDifficulty: Easy", font=("Arial", 10), bg=easy_window_bg, justify=LEFT)
    easy_question_no_label.grid(row=9, column=0, rowspan=2)
    easy_hint_label = Label(easy_window, text="\nHint: Base 10 is normal numbers.", font=("Arial", 10), bg=easy_window_bg)
    easy_hint_label.grid(row=9, column=3, columnspan=2)
    easy_question_label = Label(easy_window, font=("Arial", 11), text="", bg=easy_window_bg)
    easy_question_label.grid(row=4, column=1, columnspan=3)
    easy_user_entry = Entry(easy_window, font=("Arial", 12), width=12)
    easy_user_entry.grid(row=5, column=2)
    easy_user_entry.bind("<Return>", lambda event: check_answer(easy_user_entry, "easy"))
    easy_submit_button = Button(easy_window, text="Submit", command=lambda: check_answer(easy_user_entry, "easy"), width=10)
    easy_submit_button.config(bg="#b1c2ab")
    easy_submit_button.grid(row=6, column=2)
    easy_result_label = Label(easy_window, text="", font=("Arial", 11), bg=easy_window_bg)
    easy_result_label.grid(row=7, column=1, columnspan=3)
    easy_user_entry.config(state="normal")
    # This is the brains of the program making all of the numbers for the user to convert.
    answer = 0
    points = 0
    def load_question():
        global question_no, answer, points
        easy_user_entry.config(state="normal")
        easy_user_entry.bind("<Return>", lambda event: check_answer(easy_user_entry, "easy"))
        sw = StopWatch(easy_window)
        if question_no <= 10:
            easy_question_no_label.config(text="Level: "+str(question_no)+"/10\nDifficulty: Easy")
        if question_no > 10:
            easy_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10")
            easy_submit_button.config(state="disabled")
            easy_user_entry.config(state="disabled")
            return sw.Stop()
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
                easy_question_label.config(text="What is "+str(binary_int)+" (binary) in base 10")
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
                easy_question_label.config(text="What is "+str(decimal_int)+" in binary")
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
    global answer, points, medium_result_label, medium_window, load_question, question_no
    medium_window = Toplevel(root)
    medium_window.geometry("650x400")
    medium_window.title("Difficulty: Medium")
    medium_window.configure(bg = medium_window_bg) 
    # Makes all of the needed buttons and labels
    stop_medium = Button(medium_window, text="Back", command=medium_window.destroy, height=1, width=10)
    stop_medium.config(bg="#d7caa4")
    stop_medium.grid(row=1, column=4)
 
    medium_window.resizable(False, False)
    
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
    
    if timer_toggle == True:
        sw = StopWatch(medium_window)
        sw.grid(row=0, column=4)
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=medium_window_bg)
        sw.config(bg=medium_window_bg)
        sw.Start()
    else:
        medium_window.rowconfigure(2, minsize=22)
    
    question_no = 1
    medium_question_no_label = Label(medium_window, text="Level: "+str(question_no)+"/10\nDifficulty: Medium", font=("Arial", 10), bg=medium_window_bg, justify=LEFT)
    medium_question_no_label.grid(row=9, column=0, rowspan=2)
##    medium_hint_label = Label(medium_window, text="\nHint: The subscript number is the base.", font=("Arial", 10), bg=medium_window_bg)
##    medium_hint_label.grid(row=9, column=3, columnspan=2)
    medium_question_label = Label(medium_window, font=("Arial", 11), text="", bg=medium_window_bg)
    medium_question_label.grid(row=4, column=1, columnspan=3)
    medium_user_entry = Entry(medium_window, font=("Arial", 12), width=12)
    medium_user_entry.grid(row=5, column=2)
    medium_user_entry.bind("<Return>", lambda event: check_answer(medium_user_entry, "medium"))
    medium_submit_button = Button(medium_window, text="Submit", command=lambda: check_answer(medium_user_entry, "medium"))
    medium_submit_button.grid(row=6, column=2)
    medium_result_label = Label(medium_window, text="", font=("Arial", 11), bg=medium_window_bg)
    medium_result_label.grid(row=7, column=1, columnspan=3)
    
    # This is the brains of the program making all of the numbers for the user to convert.
    answer = 0
    points = 0
    def load_question():
        global question_no, answer, points
        if question_no <= 10:
            medium_question_no_label.config(text="Level: "+str(question_no)+"/10\nDifficulty: Medium")
        if question_no > 10:
            medium_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10")
            medium_submit_button.config(state="disabled")
            medium_user_entry.config(state="disabled")
            sw.Stop
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
                medium_question_label.config(text="What is "+str(binary_int)+" (Binary) in Decimal")
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
                answer = decimal_int
                medium_question_label.config(text="What is "+str(octal_int)+" (Octal) in Decimal")
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
                divider = random
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
                octal_int = int(octal)
                binary_int = int(binary)
                answer = binary_int
                medium_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Binary")
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
                medium_question_label.config(text="What is "+str(decimal_int)+" (Decimal) in Octal")
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
                medium_question_label.config(text="What is "+str(octal_int)+" (Octal) in Binary")
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
                medium_question_label.config(text="What is "+str(octal_int)+" (Octal) in Decimal")
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
    global expert_window
    expert_window = Toplevel(root)
    expert_window.geometry("650x400")
    expert_window.title("Difficulty: Expert")
    expert_window.configure(bg = expert_window_bg) 
    # Makes all of the needed buttons and labels
    stop_expert = Button(expert_window, text="Back", command=expert_window.destroy, height=1, width=10)
    stop_expert.config(bg="#ca8c8c")
    stop_expert.grid(row=1, column=4)

    expert_window.resizable(False, False)
    
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
    
    if timer_toggle == True:
        sw = StopWatch(expert_window)
        sw.grid(row=0, column=4)
        sw.MakeLabel()
        sw.tmr_lbl.config(bg=expert_window_bg)
        sw.config(bg=expert_window_bg)
        sw.Start()
    else:
        expert_window.rowconfigure(2, minsize=22)

    question_no = 1
    expert_question_no_label = Label(expert_window, text="Level: "+str(question_no)+"/10\nDifficulty: expert", font=("Arial", 10), bg=expert_window_bg, justify=LEFT)
    expert_question_no_label.grid(row=9, column=0, rowspan=2)
    expert_hint_label = Label(expert_window, text="\nHint: The subscript number is the base.", font=("Arial", 10), bg=expert_window_bg)
    expert_hint_label.grid(row=9, column=3, columnspan=2)
    expert_question_label = Label(expert_window, font=("Arial", 11), text="", bg=expert_window_bg)
    expert_question_label.grid(row=4, column=1, columnspan=3)
    expert_user_entry = Entry(expert_window, font=("Arial", 12), width=12)
    expert_user_entry.grid(row=5, column=2)
    expert_user_entry.bind("<Return>", lambda event: check_answer(expert_user_entry, "expert"))
    expert_submit_button = Button(expert_window, text="Submit", command=lambda: check_answer(expert_user_entry, "expert"))
    expert_submit_button.grid(row=6, column=2)
    expert_result_label = Label(expert_window, text="", font=("Arial", 11), bg=expert_window_bg)
    expert_result_label.grid(row=7, column=1, columnspan=3)
    
    # This is the brains of the program making all of the numbers for the user to convert.
    answer = 0
    points = 0
    def load_question():
        global question_no, answer, points
        if question_no <= 10:
            expert_question_no_label.config(text="Level: "+str(question_no)+"/10\nDifficulty: expert")
        if question_no > 10:
            expert_result_label.config(text="Quiz complete! Your score: "+str(points)+"/10")
            expert_submit_button.config(state="disabled")
            expert_user_entry.config(state="disabled")
            sw.Stop
            return
        # Generate question:
        this_to = int(rand(1,4)) # 1 is binary 2 is decimal 3 is octal 4 is hex (4 cant be called on medium)
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
                expert_question_label.config(text="What is "+str(binary_int)+" (binary) in base 10")
            elif this == 2: # Octal
                pass
            elif this == 3: # Hex
                pass
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
                expert_question_label.config(text="What is "+str(decimal_int)+" in binary")
            elif this == 2: # Octal
                pass
            elif this == 3: # Hex
                pass
            else:
                error("outside_val")
        elif this_to == 2: # Octal to
            this = int(rand(1,3))
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
                expert_question_label.config(text="What is "+str(decimal_int)+" in binary")
            elif this == 2: # Octal
                pass
            elif this == 3: # Hex
                pass
            else:
                error("outside_val")
        elif this_to == 2: # Hex to
            this = int(rand(1,3))
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
                expert_question_label.config(text="What is "+str(decimal_int)+" in binary")
            elif this == 2: # Octal
                pass
            elif this == 3: # Hex
                pass
            else:
                error("outside_val")
        else:
            error("outside_val")

        expert_user_entry.delete(0, tk.END)
        expert_result_label.config(text="")
        question_no += 1
   
    load_question()
    
def check_answer(entry, difficulty, event=None):
    global answer, points, easy_result_label, easy_window, medium_window, medium_result_label, expert_window, expert_result_label, load_question, easy_user_entry
    user_input = entry.get().strip()

    if not user_input.isdigit():
        messagebox.showerror("Error", "Answer must be a number.")
        return
    if difficulty == "easy":
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
    elif difficulty == "medium":
        if int(user_input) == answer:
            points += 1
            medium_result_label.config(text="Correct!")
        else:
            medium_result_label.config(text="Incorrect.\nThe correct answer was "+str(answer))

        medium_window.after(1500, load_question)
        return entry.delete(0, tk.END)


def really_quit(): # Askes the user if they really want to quit (this is not called on file-quit)
    quit_window = Toplevel(root)
    quit_window.geometry("250x50")
    quit_window.title("Really Quit?")
    really_quit_label = Label(quit_window, text="Do You Really Want To Quit?", width=25).grid(row=0, column=1, columnspan=3)
    yes_button = Button(quit_window, text="Yes", command=root.destroy, width=10, bg=expert_window_bg).grid(row=1, column=1)
    no_button = Button(quit_window, text="No", command=quit_window.destroy, width=10, bg=easy_window_bg).grid(row=1, column=3)
    quit_window.columnconfigure(0, minsize=35)
    quit_window.columnconfigure(1, minsize=10)
    quit_window.columnconfigure(2, minsize=20)
    quit_window.columnconfigure(3, minsize=10)
    quit_window.columnconfigure(4, minsize=35)
    quit_window.resizable(False, False)
    
def main(): # Root window setup makes the user choose a difficulty and welcomes the user
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
    
    menubar = Menu(root) # Menu bar
    file_menu = Menu(menubar, tearoff=0) # Settup the main dropdowns
    settings_menu = Menu(menubar, tearoff=0)
    timer_settings = Menu(settings_menu, tearoff=0)
    help_menu = Menu(menubar, tearoff=0)
    
    menubar.add_cascade(label="File", menu=file_menu) # File
    file_menu.add_command(label="Exit", command=root.destroy)
    
    menubar.add_cascade(label="Settings", menu=settings_menu) # Settings
    settings_menu.add_cascade(label="Timer", menu=timer_settings) # Adds timer on/off
    timer_settings.add_radiobutton(label="Enabled", command=timer_on) # Timer on
    timer_settings.add_radiobutton(label="Disabled", command=timer_off) # Timer off
    root.config(menu=menubar)
    
    help_menu.add_command(label="About...", command=about) # About...
    menubar.add_cascade(label="Help", menu=help_menu)
    root.config(menu=menubar)
    
    root.mainloop()
    
main()
