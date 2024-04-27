import customtkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.CTk()
root.title("Simple Calculator")

entry = tk.CTkEntry(root, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
col = 0
for button in buttons:
    btn = tk.CTkButton(root, text=button, font=("Arial", 18))
    btn.bind("<Button-1>", on_button_click)
    btn.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()