import tkinter as tk
from tkinter.constants import BOTH, LEFT, X, YES

class App(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master, background='red')
        self.pack(expand = YES, fill = BOTH)
        self.createWidgets()
    
    def createWidgets(self):
        

        self.label1 = tk.Label(self, text = "Input: ", bg = 'green')
        self.label1.pack(fill = tk.X)
        self.entrybox1 = tk.Entry(self, cursor= 'hand2', font = ('Century 15 bold'))
        self.entrybox1.pack()
        self.contents1 = tk.IntVar()
        self.contents1.set(0)
        self.entrybox1["textvariable"] = self.contents1
        self.entrybox1.bind('<Key-Return>', self.message)
        self.label2 = tk.Label(self, text = "Press \"Enter\" to get results ")
        self.label2.pack(fill = X)
        self. btn1 = tk.Button(self, text = 'Display List of Results', command = self.message)
        self.btn1.pack()

       


     # create another window where the user will seee his results.
     # he will be able to reset, delete results. 

    def message(self, event):
        print("Hello World")



app = App()
# edits windows size
app.master._root().geometry("200x150")
app.master.title('Calculator')



app.mainloop()
