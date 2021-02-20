import pyautogui  # import PyAutoGUI library
from tkinter import * 
 
root = Tk()
root.geometry('400x200')
 
# define a method which take screenshot
def take():
    image = pyautogui.screenshot("screenshot.png")
 
l1 = Label(text='SCREENSHOT GUI APP',font=('arial',18,'bold'),fg='red')
l1.pack(pady=10)

l1 = Label(text='Click Button To Take Screenshot',font=('arial',10,'bold'))
l1.pack(pady=10)

shot_btn = Button(root,text="Click Me",command=take,font=('arial',12,'bold'),fg='green')
shot_btn.pack(pady=10)

root.mainloop()