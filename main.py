import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles = float(entry.get())
    km = miles * 1.60934
    output_label.config(text=f"{miles} miles is equal to {km:.2f} kilometers")

# Create the main window
# window = tk.Tk()
window = ttk.Window(themename="journal")
window.title("My First GUI Program")
window.geometry("350x200")

# Create a label
title_label = ttk.Label(master = window, text="Miles to Kilometers Converter", font="Calibri 24 bold")
title_label.pack()

# Create an input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side='left', padx=20)
button.pack(side='left')
input_frame.pack(pady=20)

# Create an output field
output_label = ttk.Label(master = window, text="Output", font="Calibri 24")
output_label.pack()

# Run the main loo
window.mainloop()