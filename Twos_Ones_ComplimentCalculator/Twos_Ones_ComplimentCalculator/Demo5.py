from tkinter import*

window = Tk()

Label1 = Label(window, text = "Rambo")
Label2 = Label(window, text = "Cobe")

# using the grid layout 
Label1.grid(row = 0, column=0)
Label2.grid(row = 1, column=5)




window.mainloop()