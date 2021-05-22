from tkinter import *
from datetime import datetime, time, timedelta

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- Time Stamps and Formatting ------------------------------- #
now = datetime.now()
dt_string = now.strftime("%I:%M %p").strip("0")
print("time =", dt_string)
youtube_time = datetime.combine(now.date(), time(hour=18, minute=30, second=0))
youtube_string = youtube_time.strftime('%I:%M %p').strip('0')
print(f"Youtube time starts at {youtube_string}")
time_left = youtube_time - now
time_left_str = (str(time_left))
hours = time_left_str.split(':')[0]
minutes = time_left_str.split(':')[1]
print(hours)
print(minutes)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("YouTube Countdown")
window.config(padx=50, pady=50, bg=YELLOW)


title_label = Label(text="YouTube Countdown", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
title_label.pack()

canvas = Canvas(width=500, height=400, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(50, 50, text=f"The current time is {dt_string}", fill=PINK, font=(FONT_NAME, 16, "bold"), anchor=NW)
youtube_text = canvas.create_text(50, 100, text=f"YouTube starts at {youtube_string}", fill=PINK, font=(FONT_NAME, 16, "bold"), anchor=NW)
time_left_hours = canvas.create_text(50, 150, text=f"Hours: {hours}", fill=GREEN, font=(FONT_NAME, 20, "bold"), anchor=NW)
time_left_minutes = canvas.create_text(50, 200, text=f"Minutes: {minutes}", fill=GREEN, font=(FONT_NAME, 20, "bold"), anchor=NW)

canvas.pack()





window.mainloop()
