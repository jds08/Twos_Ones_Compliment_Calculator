from tkinter import *

# used to avoid name clashes
import tkinter as tk
from tkinter.messagebox import showinfo

class App(tk.Frame):
    
    def __init__ (self, master=None):
        super().__init__(master)
        self.grid()

        # Creating our label  and attaching it to our frame(self)
        tk.Label(self, text = "Enter a decimal number: ").grid(column = 0, row = 6)
        # Creating our entry widget
        self.entrythingy = tk.Entry()
        # Attaching it to the frame
        self.entrythingy.pack()
        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("000")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                            self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
               self.contents.get())




root = tk.Tk()
# create the application
myapp = App(root)

# editing my window 
myapp.master.title("Calculator")
myapp.master.maxsize(1000, 400)


# start the program
myapp.mainloop()



 

