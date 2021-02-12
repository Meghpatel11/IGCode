from tkinter import *

root = Tk()
root.title("Change Color")
root.geometry('300x300')

def bg():
    userbg = setcolor.get()
    root.config(bg=userbg)

setcolor = StringVar()
# setcolor.set("white")

colorlist = OptionMenu(root,setcolor,"White","black")
colorlist.grid(row=0,sticky=NE)
colorlist.config(font=('arial',8),bg='orange')

Button(root,command=bg,text='THEAM',bg='orange',font=('arial',8)).grid(column=1,row=0,sticky=E)

#Button(root,command=bg,text='ChangeBG',fg='green',font=('arial',8)).place(x=120,y=150)

root.mainloop()