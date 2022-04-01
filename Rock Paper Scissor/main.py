from tkinter import *
import random
# Window's Initialization
window = Tk()
window.geometry('500x500')
window.resizable(3,3)
window.title('Rock, Paper, Scissor')
window.config(bg='Black')
# Heading
Label(window, text='Rock, Paper, Scissor', font='arial 20 bold', bg='black').pack()
# User Choice
user = StringVar()
Label(window, text='Choose One: Rock, Paper, Scissor', font='arial 20 bold', bg='black').place(x=20, y=50)
Entry(window, font='arial 20', textvariable=user, bg='white').place(x=70, y=100)
# Computer Choice
comp = random.randint(1,3)
if comp == 1:
    comp = 'Rock'
elif comp == 2:
    comp = 'Paper'
else:
    comp = 'Scissor'
# Function to Play
conclusion = StringVar()
def game():
    user_choice = user.get()
    if user_choice == comp:
        conclusion.set('Tada, You both Choosed Same')
    elif user_choice == 'Rock' and comp == 'Paper':
        conclusion.set('You loose as you choosed rock and Computer choosed paper')
    elif user_choice == 'Paper' and comp == 'Rock':
        conclusion.set('You win as you choosed paper and Computer choosed rock')
    elif user_choice == 'Rock' and comp == 'Scissor':
        conclusion.set('You win as you choosed rock and Computer choosed scissor')
    elif user_choice == 'Scissor' and comp == 'Rock':
        conclusion.set('You loose as you choosed scissor and Computer choosed rock')
    elif user_choice == 'Paper' and comp == 'Scissor':
        conclusion.set('You loose as you choosed paper and Computer choosed scissor')
    elif user_choice == 'Scissor' and comp == 'Paper':
        conclusion.set('You win as you choosed scissor and Computer choosed paper')
    else:
        conclusion.set('invalid choice, Choose one: Rock, Paper, Scissor')
# Function to Reset
def again():
    conclusion.set("")
    user.set("")
# Function for exiting
def stop():
    window.destroy()

# Buttons
Entry(window, font='arial 10 bold', textvariable= conclusion, bg ='white', width = 50).place(x=25, y = 250)
Button(window, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=game).place(x=150, y=190)
Button(window, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=again).place(x=70, y=310)
Button(window, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=stop).place(x=230, y=310)
window.mainloop()