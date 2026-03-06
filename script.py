# ***** IMPORTS *****
import tkinter as tk

# ***** VARIABLES *****
running = False
hours, minutes, seconds = 0, 0, 0
update_time = None   # define before use

# ***** FUNCTIONS *****

def start():
    global running
    if not running:
        running = True
        update()

def pause():
    global running, update_time
    if running and update_time:
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running, hours, minutes, seconds, update_time

    if running and update_time:
        stopwatch_label.after_cancel(update_time)
        running = False

    hours, minutes, seconds = 0, 0, 0
    stopwatch_label.config(text="00:00:00")


def update():
    global hours, minutes, seconds, update_time

    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0

    if minutes == 60:
        hours += 1
        minutes = 0

    hours_string = f'{hours:02}'
    minutes_string = f'{minutes:02}'
    seconds_string = f'{seconds:02}'

    stopwatch_label.config(text=f"{hours_string}:{minutes_string}:{seconds_string}")

    update_time = stopwatch_label.after(1000, update)


# ***** WINDOW *****
root = tk.Tk()
root.geometry("485x220")
root.title("Stopwatch")

# ***** LABEL *****
stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 80))
stopwatch_label.pack()

# ***** BUTTONS *****
start_button = tk.Button(root, text="Start", height=5, width=7, font=("Arial", 20), command=start)
start_button.pack(side=tk.LEFT)

pause_button = tk.Button(root, text="Pause", height=5, width=7, font=("Arial", 20), command=pause)
pause_button.pack(side=tk.LEFT)

reset_button = tk.Button(root, text="Reset", height=5, width=7, font=("Arial", 20), command=reset)
reset_button.pack(side=tk.LEFT)

quit_button = tk.Button(root, text="Quit", height=5, width=7, font=("Arial", 20), command=root.quit)
quit_button.pack(side=tk.LEFT)

# ***** RUN *****
root.mainloop()