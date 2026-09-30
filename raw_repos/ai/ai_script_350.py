"""Print the Hello World message using the Tkinter module in Python"""
import tkinter as tk

# Create the main window
window = tk.Tk()

# Create the label with the text
hello_label = tk.Label(window, text="Hello World")

# Pack the label to the window
hello_label.pack()

# Main loop
window.mainloop()