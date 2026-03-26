import tkinter as tk
from tkinter import messagebox

FILE_PATH = "D:/Private;/Likhayi/Quote.txt"

def save_quote():
    quote = entry.get("1.0", tk.END).strip()
    if quote == "":
        messagebox.showwarning("Empty Input", "Please type a quote before saving.")
        return
    with open(FILE_PATH, "a") as f:
        f.write(quote + "\n")
        f.write("------------------------------------------------------------------------------\n")
    entry.delete("1.0", tk.END)  # clear text box
    messagebox.showinfo("Saved", "Your quote has been saved.")

# Create main window
root = tk.Tk()
root.title("Quote Saver")
root.geometry("400x300")

# Text area for quote
entry = tk.Text(root, height=10, width=40, wrap="word")
entry.pack(pady=10)

# Save button
save_btn = tk.Button(root, text="Save Quote", command=save_quote)
save_btn.pack(pady=5)

# Exit button
exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=5)

root.mainloop()
