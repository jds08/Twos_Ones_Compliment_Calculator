from tkinter import *
from tkinter.messagebox import showinfo
class MyGui(Frame):
   def __init__(self, parent=None):
       Frame.__init__(self, parent)
   
       button = Button(self, text='press', command=self.reply)
       button.pack()
   def reply(self):
       showinfo(title='popup', message='Button pressed!')

# The variable __name__ for the file/module that is run will be always __main__.
# But the __name__ variable for all other modules that are being imported will 
# be set to their module's name.

if __name__ == '__main__':
   window = MyGui()
   window.pack()
   window.mainloop()





