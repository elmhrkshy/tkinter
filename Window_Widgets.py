import tkinter as tk
from tkinter import ttk

def button_func():
    print("Button clicked")

def exercise_button_func():
    print("Hello")

# Create a window
window = tk.Tk()
window.title("Window & Widgets")
window.geometry("800x500")

# Create tk widgets (text)
# tk.Text(master = window).pack()
text = tk.Text(master = window)
text.pack()

# Create ttk widgets (label)
label = ttk.Label(master = window, text="This is a test")
label.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

excercise_label = ttk.Label(master = window, text="My Label")
excercise_label.pack()

# ttk button
button = ttk.Button(master = window, text="A Button", command = button_func)
button.pack()

# excerise
# add one more text label and a button with a function that prints "Hello"
# the label should say "my label" and be between the entry widget and the button
# exercise_entry = ttk.Entry(master = window)
# exercise_entry.pack()

# exercise_button = ttk.Button(master = window, text="Exercise Button", command = exercise_button_func)
exercise_button = ttk.Button(master = window, text="Exercise Button", command = lambda: print("Hello"))
exercise_button.pack()

# Run the window
# mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
window.mainloop()

# The window is created but it is not visible. The window is created and the mainloop() is running. The window is not visible because it is not given any size or title.