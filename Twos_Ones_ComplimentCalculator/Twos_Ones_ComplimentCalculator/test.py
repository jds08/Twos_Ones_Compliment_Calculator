from tkinter import*
from tkinter import ttk

# Creates a window 
Window = Tk()  

# Adds a frame widget where the other widgets will be hold
frame = ttk.Frame(Window, padding= 10)

# Declares the frame layout
frame.grid()

#Creates a label widget and adds it to the frame
# .grid() specifies where the the widget should be placed.
label = ttk.Label(frame, text = "Not me")
print("Label:")

# checking the configuration options of a widget using the .configure() method
print(label.configure().keys())
print("\nLabel Specific:")

#set() method is used to create a collection of objects that are un ordered. No duplicate elements.
# specific configurations to a widget class
print(set(label.configure().keys()) - frame.configure().keys())