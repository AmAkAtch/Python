from tkinter import *
import math

#constants
YELLOW = "#FFD65A"
CANVAS_WIDTH, CANVAS_HEIGHT = 300, 300
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
FOCUS_MIN = 25

#VARIABLES
pomodoro_counter = 0
total_cycles = 0
timer_job = None
is_doro_on = False
is_break_on = False

def update_time(seconds, message):
    """Take Seconds to Update timer every second and Message to Display when Timer ends"""
    display_seconds = seconds % 60
    display_min = math.floor(seconds/60)

    if display_seconds <10:
        window.lift()
        display_seconds = f'0{display_seconds}'

    canvas.itemconfigure(timer, text=f'{display_min}:{display_seconds}')

    if(seconds>0):
        global timer_job
        timer_job = window.after(1000, update_time, seconds-1, message)
    else:
        status_label.config(text=message)

def start_break():
    """Function to Start Break"""

    global pomodoro_counter, total_cycles, timer_job, is_break_on, is_doro_on

    if is_break_on:
        return
    
    is_doro_on = False
    is_break_on = True

    status_label.config(text="Break is On 🎉")
    counter.config(text=f'Total Cycles: {total_cycles}')

    if timer_job:
        window.after_cancel(timer_job)   # cancel the scheduled countdown
        timer_job = None

    if pomodoro_counter<3:
        pomodoro_counter += 1
        update_time(SHORT_BREAK_MIN*60, "Break Complete, Start next Pomodoro!!")
    else:
        pomodoro_counter=0
        update_time(LONG_BREAK_MIN*60, "Break Complete, Start next Pomodoro!!")

def handle_start():
    """Function to handle Start Button"""

    status_label.config(text="Pomodoro is in progress focus on Work 📚")
    global timer_job, is_break_on, is_doro_on, total_cycles
    
    if is_doro_on:
        return
    
    total_cycles += 1
    is_doro_on = True
    is_break_on = False

    if timer_job:
        window.after_cancel(timer_job)   # cancel the scheduled countdown
        timer_job = None

    update_time(FOCUS_MIN*60, "Pomodoro Complete, Start Break!!!")

def handle_reset():

    global pomodoro_counter, timer_job, counter, is_break_on, is_doro_on
    
    if is_break_on:
        return
    
    is_doro_on = False
    is_break_on = False

    if timer_job:
        window.after_cancel(timer_job)   # cancel the scheduled countdown
        timer_job = None

    pomodoro_counter = 0
    counter = 0
    canvas.itemconfigure(timer, text="00:00")


window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW)

title = Label(text="POMODORO TIMER", font=("Times New Roman", 20) ,bg=YELLOW)
title.grid(row=0, column=1, pady=10)

counter = Label(text=f'Total Cycles: {total_cycles}', bg=YELLOW, font=("Ariel"))
counter.grid(row=1, column=1)

IMAGE = PhotoImage(file="day28_pomodoro/tomato.png")
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=IMAGE)
timer = canvas.create_text(CANVAS_WIDTH/2, CANVAS_WIDTH/2+10,text=f'00:00',fill="white", font=("Arial", 30, "bold"))
canvas.grid(row=2, column=1)

start_button = Button(text="Start", command=handle_start)
start_button.grid(row=3, column=0)

break_button = Button(text="Break", command=start_break)
break_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=handle_reset)
reset_button.grid(row=3, column=2)

status_label = Label(text="", font=("Arial", 14), bg=YELLOW)
status_label.grid(row=4, column=1, pady=2)



window.mainloop()