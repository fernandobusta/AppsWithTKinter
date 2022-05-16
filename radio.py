from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Hello, this is code')
root.iconbitmap('images/calc.ico')



#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: clicked(r.get())).pack()

MODES = [
	("Perpperoni","Perpperoni"),
	("Cheese","Cheese"),
	("Mushroom","Mushroom"),
	("Onion","Onion")
]

pizza = StringVar()
pizza.set("Perpperoni")

for text, mode in MODES:
	Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()

myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
