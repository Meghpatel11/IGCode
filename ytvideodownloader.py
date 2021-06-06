from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube Video Downloder")
root.geometry('500x300')
root.config(bg='yellow')

Label(root,text='Downlode YouTube Video',font=('Helvetica',18,'bold'),bg='yellow').grid(row=0,padx=120,pady=5)

Label(root,text='Enter Url',font=('Helvetica',18),fg='black',bg='yellow').grid(row=1,padx=120,pady=25)

user_url=Entry(root, font=("Helvetica","16"))
user_url.grid(row=2,padx=120,pady=5)

def downloader():
    url = YouTube(str(user_url.get()))
    video = url.streams.first()
    video.download()
    Label(root,text='Video Downloaded in working directory',font=('Helvetica',12,'bold'),bg='yellow').grid(row=3,padx=120,pady=10)

Button(root,text='Download',command=downloader,fg='yellow',bg='black',font=('Helvetica',10,'bold')).grid(row=4,padx=120,pady=25)
root.mainloop()

