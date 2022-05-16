from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Hello, this is code')
root.iconbitmap('images/calc.ico')
root.geometry("400x400")


# Drop down boxes

def show():
	myLabel = Label(root, text=clicked.get()).pack()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday"
]

clicked = StringVar()
clicked.set(options[0])

#have to put a star
drop  = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
