from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='black', borderwidth=5)
e.pack()
#to get the info typed in
#e.get()
#value already inside
e.insert(0, 'Enter your name:')

def myClick():
	hello = 'Hello ' + e.get()
	myLabel = Label(root,text=hello)
	myLabel.pack()

#No parenthesis on the function call
myButton = Button(root, text='Enter your name', command=myClick)
myButton.pack()

root.mainloop()