from tkinter import *

root = Tk()

# padx parameter edits wigets size
button = Button(root, text= 'Click me', padx=70)
button.grid(row=0, column=0)

root.mainloop()