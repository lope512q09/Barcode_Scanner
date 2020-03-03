from tkinter import *

# Making the window.
root = Tk()
root.geometry('1100x600')
root.configure(bg='#bfbd92')

# Making entry widget.
e = Entry(root, bg='#eeeeee', borderwidth=1)
e.pack()
e.insert(0, "Enter your name:")


def my_click():
    hello = "Hello" + " " + e.get()
    my_label = Label(root, text=hello, bg='#bfbd92')
    my_label.pack()


# Creating a button widget.
my_button = Button(root, text="Enter your name", command=my_click, bg='white')
my_button.pack()

# Creating the loop to keep window open and run the GUI.
root.mainloop()
