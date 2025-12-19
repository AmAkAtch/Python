import pandas as pd
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
flip_timer = None


#import to_learn.csv to data
    #When exception(First run) import french_words.csv to data
    #convert data into dictionary
try:
    data = pd.read_csv("day31_flashcard/data/to_learn.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    data = pd.read_csv("day31_flashcard/data/french_words.csv")
finally:
    data_dictionary = data.to_dict("records")


#function to select new current word
def select_new_word():
    #form the dcata dictonary select one random word and save it as current word
    global current_word
    current_word = random.choice(data_dictionary)


#function to flip the card
def flip_card():
    #change the background to card_back
    #chagne title text to English
    #load the English word from current word
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(language_title, text = "English")
    canvas.itemconfig(word, text=current_word["English"])
    

#function to go to next card
def next_card():
    global flip_timer
    #Stop any running counter
    #Select new Current word
    #replace the card_background
    #load the french word from current word
    #start the 3 second counter and call function to flip the card
    if flip_timer:
        window.after_cancel(flip_timer)

    select_new_word()
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(language_title, text="French")
    canvas.itemconfig(word, text=current_word["French"])
    flip_timer = window.after(3000, flip_card)
    

#function to update the csv
def update_csv():
    global data
    #remove the current word from the data_dictionary
    #write the current data dictionary to to_learn csv
    #call next card function
    data = data[data["French"] != current_word["French"]]
    data.to_csv("day31_flashcard/data/to_learn.csv", index=False)
    next_card()

#define window with tkinter
window = Tk()
window.title("Lanugage Flash Cards")
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)

#Create Canvas
    #Create photoimage for images Card_back, Card_front, right and wrong
canvas = Canvas(width=800, height=530, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

    #Display language and Word on the Card
    #Flip the card after 3 second
card_front = PhotoImage(file="day31_flashcard/images/card_front.png")
card_back = PhotoImage(file="day31_flashcard/images/card_back.png")
card_background = canvas.create_image(400, 265, image=card_front)
language_title = canvas.create_text(400, 100, text="Language", font=("Arial", 20, "bold", "italic"))
word = canvas.create_text(400, 250, text="Word", font=("Ariel", 50, "bold"))
next_card()

    #clicked on wrong button just normal display next card
btn_wrong_img = PhotoImage(file="day31_flashcard/images/wrong.png")
btn_wrong = Button(image=btn_wrong_img, command=next_card)
btn_wrong.grid(row=1, column=0)

    #Clicked on right button Go remove the word from data and update the to_learn csv
btn_right_img = PhotoImage(file="day31_flashcard/images/right.png")
btn_right = Button(image=btn_right_img, command=update_csv)
btn_right.grid(row=1, column=1)

#keep the program running
window.mainloop()