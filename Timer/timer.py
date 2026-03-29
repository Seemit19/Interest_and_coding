import tkinter as tk

time_left = 0
job_id = None

def start_timer():
    global time_left, job_id
    
    if job_id is not None:
        return
    
    time_left = int(entry.get())
    countdown()

def countdown():
    global time_left, job_id
    
    if time_left > 0:
        label.config(text=f"{time_left} sec")
        time_left -= 1
        job_id = root.after(1000, countdown)
    else:
        label.config(text="Time's up!")
        job_id = None

def pause_timer():
    global job_id
    if job_id is not None:
        root.after_cancel(job_id)
        job_id = None

def resume_timer():
    global job_id
    if job_id is None and time_left > 0:
        countdown()

root = tk.Tk()
root.title("Timer")
root.geometry("200x200")

entry = tk.Entry(root)
entry.pack(pady=10)

label = tk.Label(root, text="Time")
label.pack(pady=5)

tk.Button(root, text="Start", command=start_timer).pack(pady=5)
tk.Button(root, text="Pause", command=pause_timer).pack()
tk.Button(root, text="Resume", command=resume_timer).pack()

root.mainloop()
