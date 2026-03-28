import tkinter as tk

def start_timer():
    time = entry.get()
    countdown(time)
    # pause_button = tk.Button(root,text = "Pause timer" , command = pause)
    # pause_button.pack()
    # resume_button = tk.Button(root,text = "Resume timer" , command = resume)
    # resume_button.pack()


def countdown(time):    
    time = int(time)
    if time > 0:
        label.config(text = time)
        time -= 1
        root.after(1000,countdown,time)
    else :
        label.config(text = "Time is up!")

# def pause():
    
#     pass

# def resume():
#     pass

# Main window
root = tk.Tk()
root.title("Timer")
root.geometry("200x200")

#area to enter time
entry = tk.Entry(root)
entry.pack(pady = 10)

#Information showcase
label = tk.Label(root , text = "Time")
label.pack(pady=5)

#Button to start timer
start_button = tk.Button(root , text= "Start" , command = start_timer)
start_button.pack(pady=5)

root.mainloop()
