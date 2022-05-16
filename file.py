from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

#open file dialog box
root = Tk()
root.title('Hello, this is code')
root.iconbitmap('images/calc.ico')

def open():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir="/Users/fernandobustamante/Desktop/tkinter-course/images", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
	my_label = Label(root, text=root.filename)
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_images_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open file", command=open).pack()

root.mainloop()
