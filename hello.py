from tkinter import *

#To create the window
root = Tk()

#Creating a label widget
myLabel = Label(root, text='Hello World!')
#Shoving it onto the screen
#pack -> as big as the content is
myLabel.pack()

#ends loop by clicking the cross
root.mainloop()