from tkinter import *
import pyshorteners
import clipboard

root = Tk()
root.geometry("400x200")
root.resizable(False, False)
root.title("URL Shortener")

Label(root,text="Enter URL",font=("Helvetica","16"), fg='blue').grid(row=0, pady=5,padx=5)

# url entry
url_input = Entry(root, font=("Helvetica","16"))
url_input.grid(row=0, column=1, pady=5,padx=5)

#label shortened url
str_url = StringVar(root)

Label(root,textvariable=str_url,font=("Helvetica","16"),fg="yellow",bg="black").grid(row=2,column=1,padx=5,pady=5)

# copy short url 
def copy():
  try:
    clipboard.copy(str_url.get())
    print("Url copied successfully !!")
  except:
    str_url.set("Something wrong try again !!")

#short url function
def short_url():
  try:
    s = pyshorteners.Shortener()
    url = url_input.get()
    final_result = s.tinyurl.short(url)
    str_url.set(final_result)
    url_input.delete(0, END) # clear input 
  except:
    str_url.set("Enter url please !! ")

#click button to short url
Button(root,text="Short Url",padx=5,pady=5,fg='green',font=("Helvetica","12"),command=short_url).grid(row=2, pady=6)
# Copy short url button
Button(root, text="Copy",fg='red',font=("Helvetica","12"), command=copy).grid(row=3, column=1, pady=5)

root.mainloop()