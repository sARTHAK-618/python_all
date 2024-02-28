from tkinter import *

root = Tk()

def MyClick():
    myLabel = Label(root, text = "Look! I clicked a button!!")
    myLabel.pack()

myButton = Button(root, text = "click Me", command=MyClick)
myButton.pack()

root.mainloop()