import time
from tkinter import messagebox, simpledialog

work_duration = (simpledialog.askinteger("Pomodoro Timer", "Enter work duration (in minutes):"))
break_duration = (simpledialog.askinteger("Pomodoro Timer", "Enter break duration (in minutes):"))

while True:
    messagebox.showinfo("Pomodoro Timer", f"Time to work for {work_duration} minute(s)")
    time.sleep(work_duration*60)
    messagebox.showinfo("Pomodoro Timer", f"Time for a break for {break_duration} minute(s)")
    time.sleep(break_duration*60)
