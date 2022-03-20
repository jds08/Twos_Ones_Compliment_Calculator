from tkinter import * 
from tkinter.messagebox import *

class Window(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self,parent=None)
        self.pack(expand=YES, fill =BOTH)
        self.createWidgets()
        self.master.title("Calculator")

    
    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolBar()
        self.makeEntry()  
     
        

    def makeEntry(self):
        L = Label(self, text='Input:')
        L.config(relief=SUNKEN, bg='white')
        L.pack(expand=YES, fill=BOTH)
        self.entry = Entry(self)
        self.entry.pack()
        self.contents = StringVar()
        self.contents.set("this is a variable")
        self.entry["textvariable"] = self.contents
        self.entry.bind('<Key-Return>',
                             self.print_contents)

    def makeToolBar(self):
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM,fill = X)
        Button(toolbar, text='Quit', command=self.quit).pack(side=RIGHT)
        Button(toolbar, text='Info', command=self.info).pack(side=LEFT)
    
    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu = self.menubar) # master top-level window
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Open..',command= self.notdone),
        pulldown.add_command(label = 'Quit', command=self.quit)
        self.menubar.add_cascade(label ='File', underline=0, menu=pulldown)

    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Paste', command = self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='Delete', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)

    def imageMenu(self):
        
        pulldown = Menu(self.menubar)
        img = PhotoImage('C:\..Twos_Ones_ComplimentCalculator\CalculatorDraft.png')
        pulldown.add_command(image = img, command=self.notdone)
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)

    def print_contents(self, event):




        print("Hi. The current entry content is:",
              self.contents.get())

    def info(sef):
        print("More information")

    def greeting(self):
        showinfo('Greetings')
    def notdone(self):
        showerror('Not Implemented')
    def qui(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit()

if __name__ == '__main__': Window().mainloop() 




        
























