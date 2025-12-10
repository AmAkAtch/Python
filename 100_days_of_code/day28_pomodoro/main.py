from tkinter import *

#constants
YELLOW = "#FFD65A"
CANVAS_WIDTH, CANVAS_HEIGHT = 300, 300
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5
FOCUS_MIN = 25

#VARIABLES
pomodoro_counter = 0

def handle_start():
    global pomodoro_counter
    if pomodoro_counter < 4:
        pomodoro_counter += 1
        canvas.itemconfigure(timer, text=f'')
    else:
        pomodoro_counter = 0

def handle_stop():
    global pomodoro_counter
    pomodoro_counter = 0
    canvas.itemconfigure(timer, text=f'')


window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW)

title = Label(text="POMODORO TIMER", font=("Times New Roman", 20) ,bg=YELLOW)
title.pack(pady=10)

IMAGE = PhotoImage(file="day28_pomodoro/tomato.png")
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=IMAGE)
timer = canvas.create_text(CANVAS_WIDTH/2, CANVAS_WIDTH/2+10,text=f'',fill="white", font=("Arial", 30, "bold"))
canvas.pack()

start_button = Button(text="Start", command=handle_start)
start_button.pack(side='left')

stop_button = Button(text="Stop")
stop_button.pack(side='right')


window.mainloop()