from tkinter import *
from tkcalendar import *

root = Tk()
root.title()
root.geometry('400x300')
root.resizable(False,False)
root.config(bg='orange')

cal = Calendar(root,selectmode='day',year=2021,month=1)
cal.pack(pady=10)

def get_info():
    x = cal.get_date()
    curent_date['text'] = x

Button(root,text='Get Info',command=get_info,fg='green').pack(pady=5)

curent_date = Label(root,text='',font=('Arial,18'),fg='black',bg='orange')
curent_date.pack(pady=5)

root.mainloop()