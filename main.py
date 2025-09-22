import pandas
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
word_list= {}
#Getting Data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

# Changing the Display
def next_card():
    global current_word,flip_timer
    window.after_cancel(flip_timer)
    # Getting random French word
    current_word = random.choice(word_list)
    canvas.itemconfig(language_text,text="French",fill="black")
    canvas.itemconfig(text_meaning,text = current_word["French"],fill="black")
    canvas.itemconfig(wallpaper,image=card_front)
    flip_timer = window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(language_text,text="English",fill="white")
    canvas.itemconfig(text_meaning,text=current_word["English"],fill="white")
    canvas.itemconfig(wallpaper,image=card_back)

def is_known():
    word_list.remove(current_word)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)
#Paths
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

#Setting up the Canavas
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,bd=0,highlightthickness=0)
wallpaper = canvas.create_image(405,263,image=card_front)
language_text = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
text_meaning = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

# Buttons
know_button = Button(image=right,highlightthickness=0,pady=10,command=is_known)
know_button.grid(row=1,column=1)
unknown_button = Button(image=wrong,highlightthickness=0,pady=10,command=next_card)
unknown_button.grid(row=1,column=0)
next_card()
window.mainloop()


