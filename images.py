from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Hello again')
#no funciona el icono
root.iconbitmap('/images/calc.ico')



my_img = ImageTk.PhotoImage(Image.open('pic-3.png'))
my_label = Label(image=my_img)
my_label.pack()




#button to quit
button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()
