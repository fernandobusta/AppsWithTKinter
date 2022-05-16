from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Hello, this is code')
root.iconbitmap('images/calc.ico')

def open():
	global my_img
	#just like a new window
	#can be traeted as root
	top = Toplevel()
	lbl = Label(top, text="Hello").pack()
	my_img = ImageTk.PhotoImage(Image.open("images/pic-1.png"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Screen", command=open).pack()



root.mainloop()
