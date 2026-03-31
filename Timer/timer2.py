import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("200x200")

        self.time_left = 0
        self.job_id = None
      
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.label = tk.Label(root, text="Time")
        self.label.pack(pady=5)

        tk.Button(root, text="Start", command=self.start_timer).pack(pady=5)
        tk.Button(root, text="Pause", command=self.pause_timer).pack()
        tk.Button(root, text="Resume", command=self.resume_timer).pack()

    def start_timer(self):
        if self.job_id is not None:
            return
        
        self.time_left = int(self.entry.get())
        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.label.config(text=f"{self.time_left} sec")
            self.time_left -= 1
            self.job_id = self.root.after(1000, self.countdown)
        else:
            self.label.config(text="Time's up!")
            self.job_id = None

    def pause_timer(self):
        if self.job_id is not None:
            self.root.after_cancel(self.job_id)
            self.job_id = None

    def resume_timer(self):
        if self.job_id is None and self.time_left > 0:
            self.countdown()


# main
root = tk.Tk()
app = TimerApp(root)
root.mainloop()
