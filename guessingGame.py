from tkinter import *
import random

root = Tk()
root.title("Number Guessing Game")
root.geometry("500x200")

num = random.randint(1,100)
attempts = 10

def check():
    global attempts
    global text

    attempts -=1

    user = int(entry1.get())

    if user == num:
        text.set("Well Done, You Won!!!")

    elif attempts == 0:
        text.set("You Are Out Of Attempts!")
        b1.destroy()

    elif user > num:
        text.set("Higher Value, Go to Lower one," + str(attempts) + "Left")
    elif user < num:
        text.set("Lower Value, Go to Higher one," + str(attempts) + "Left")

label = Label(root,text="Guess The Number Between 1 & 100",font=('arial',16))
label.place(x=70,y=10)

entry1 = Entry(root,width=30,bg='white',font=('arial',16))
entry1.place(x=70,y=50)

b1 = Button(root,text='Check',command=check,fg='green',font=('arial',12))
b1.place(x=210,y=85)
b2 = Button(root,text='Quit',command=root.quit,fg='red',font=('arial',12))
b2.place(x=220,y=120)

text = StringVar()
text.set("You Have 10 attempts to predict. Good Luck!!")

show_attempts = Label(root,textvariable=text,font=('arial',12))
show_attempts.place(x=90,y=155)

root.mainloop()