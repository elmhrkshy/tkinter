import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry widget
    # print(entry.get())
    entry_text = entry.get()

    # update the label widget
    # label.config(text = entry.get())
    label["text"] = entry_text
    # entry.delete(0, tk.END)
    # entry["delete"](0, tk.END)  # same as above
    entry['state'] = 'disabled'
    # print(label.configure())

# window
window = tk.Tk()
window.title("Getting & Setting widgets")

# label widget
label = ttk.Label(master = window, text="Retreive text")
label.pack()

# entry widget
entry = ttk.Entry(master = window)
entry.pack()

# button widget
button = ttk.Button(master = window, text="Button", command = button_func)
button.pack()

# excercise
# add another button that changes the text back to 'some text' and that enables entry
excercise_button = ttk.Button(master = window, text="Excercise button", command = lambda: [label.config(text="some text"), entry.config(state="enabled")])
excercise_button.pack()

# run the window
window.mainloop()