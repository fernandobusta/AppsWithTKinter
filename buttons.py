from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text='Look! I clicked a myButton')
	myLabel.pack()

#No parenthesis on the function call
myButton = Button(root, text='Click Me!', command=myClick, fg='blue', bg='red')
myButton.pack()

root.mainloop()