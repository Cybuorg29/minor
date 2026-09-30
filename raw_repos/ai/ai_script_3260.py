import tkinter as tk

root = tk.Tk()

# design the window
root.title("Calculator")
root.geometry("200x250")

# create the buttons
button1 = tk.Button(root, text="1", width=5, height=2)
button1.grid(row=0, column=0, padx=4, pady=4)

button2 = tk.Button(root, text="2", width=5, height=2)
button2.grid(row=0, column=1, padx=4, pady=4)

button3 = tk.Button(root, text="3", width=5, height=2)
button3.grid(row=0, column=2, padx=4, pady=4)

# create more buttons
# and so on

root.mainloop()