from tkinter import *

# Making the window.
root = Tk()

# Creating label widget.
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Manuel Lopez")

# Putting label onto screen.
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Creating the loop to keep window open and run the GUI.
root.mainloop()
