from tkinter import *

#To create the window
root = Tk()

#Creating a label widget
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My name is Fernando Bustamante')

#Shoving it onto the screen
#pack -> as big as the content is
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


#ends loop by clicking the cross
root.mainloop()