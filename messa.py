from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Hello, this is code')
root.iconbitmap('images/calc.ico')

def popup():
	response = messagebox.askyesno("This is my popup", "Hello World!")
	Label(root, text=response).pack()
	if response == 1:
		Label(root, text="Your clicked Yes").pack()
	else:
		Label(root, text="You clicked No").pack()


Button(root, text="Popup", command=popup).pack()



root.mainloop()
