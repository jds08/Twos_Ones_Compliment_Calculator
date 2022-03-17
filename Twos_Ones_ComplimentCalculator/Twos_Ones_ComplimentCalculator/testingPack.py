from tkinter import *
root = Tk()
# .pack() layout options
# fill fills widget space 
# expand strech and fill hte expanden space
# Label(root, text = 'Hello World', bg = 'red' ).pack( expand = YES, fill = BOTH)


Label(root, text = 'Top', bg = 'green').pack(side = TOP, expand = YES, fill = Y)
Label(root, text = 'Bottom', bg = 'yellow').pack(side = BOTTOM, expand = YES, fill = BOTH)
Label(root, text = 'Left', bg = 'purple').pack(side = LEFT, expand = YES, fill = X)
Label(root, text = 'Right', bg = 'blue').pack(side = RIGHT,fill = BOTH)


# .pack() is set to TOP by default.
# Label(root, text = 'Center').pack()

root.mainloop()

