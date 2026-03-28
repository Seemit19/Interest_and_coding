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

