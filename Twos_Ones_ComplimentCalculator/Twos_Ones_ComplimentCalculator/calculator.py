import tkinter as tk
import tkinter as tk
from tkinter.messagebox import showinfo

class App(tk.Frame):
    def __init__(self, master = None):
        super(). __init__(master)
        self.pack()
        tk.Label(self, text = "Enter a decimal number: ").pack()
        self.inputBox = tk.Entry()
        self.inputBox.pack()
        self.input = tk.StringVar()
        self.inputBox["textvariable"] = self.input

        self.inputBox.bind('<Key-Return>',
                           self.print_binary)

    def print_binary(self, event):
        print("Hello")

root = tk.Tk()
# create the application
myapp = App(root)

# editing my window 
myapp.master.title("Calculator")
myapp.master.maxsize(1000, 400)


# start the program
myapp.mainloop()