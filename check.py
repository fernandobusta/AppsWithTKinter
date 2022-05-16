from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Hello, this is code')
root.iconbitmap('images/calc.ico')
root.geometry("400x400")


var = StringVar()

def show():
	myLabel = Label(root, text=var.get()).pack()



c = Checkbutton(root, text="Check this box.", variable=var, onvalue="On", offvalue="Off")
#has to be deselected, otherwise there is big space.
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
