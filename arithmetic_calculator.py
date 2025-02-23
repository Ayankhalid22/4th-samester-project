import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry_var.get()
            if any(op in expression for op in ['+', '-', '*', '/']):
                result = eval(expression)
                entry_var.set(result)
            else:
                messagebox.showerror("Error", "Only arithmetic operations allowed")
                entry_var.set("")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry_var.set("")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Arithmetic Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.SUNKEN, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    for button in row:
        btn = tk.Button(frame, text=button, font="Arial 15", height=2, width=5)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", on_click)

root.mainloop()
