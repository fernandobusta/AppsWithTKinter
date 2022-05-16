from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

#open file dialog box
root = Tk()
root.title('Hello, this is code')
root.iconbitmap('images/calc.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=400)
#don't pack it on the same line
vertical.pack()

def slide():
	my_label = Label(root, text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()



my_btn = Button(root, text="Click me!", command=slide).pack()
root.mainloop()
