import tkinter as tk

class App(tk.Frame):
    def __init__(self, master = None):
        super(). __init__(master)
        self.pack()
        tk.Label(self, text = 'Enter a decimal number: ').pack()
        self.inputBox = tk.Entry()
        self.inputBox.pack()
        self.input = tk.StringVar()
        self.inputBox["textvariable"] = self.input

        self.inputBox.bind('<Key-Return',
                           self.print_binary)

def print_binary(self, event):
    # mod and integer division 
    number = self.input,get()
    while(number > 0 ){
        
        
        }
    
   




       



