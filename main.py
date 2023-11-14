import math
# from datetime import time

import winsound
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1/3
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0
def start_timer():
    global  reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break", fg=RED, font=(FONT_NAME, 30, "bold"), bg=YELLOW )
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Short Break", fg=PINK, font=(FONT_NAME, 30, "bold"), bg=YELLOW )
    else:
        count_down(work_sec)
        title.config(text="Work Time", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def alarm_sound():
    for _ in range(5):  # Number of beeps
        winsound.Beep(1500, 2000)  # 1500 Hz for 500 milliseconds
        time.sleep(0.25)  # Pause between beeps
def count_down(count):
    global  timer
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    #dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        #play sound
        alarm_sound()
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=90, pady=40, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title.grid(column=1, row=0)


#canvas widget
canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
img_pomo = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img_pomo)
time_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))  # *args-> unlimited positional arguments and **kwargs-> unlimited keyword arguments
canvas.grid(column=1,row=1)



start_button = Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()