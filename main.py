from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer and UI elements to their initial state."""
    global reps
    window.after_cancel(timer)  # Cancel the current timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer text
    title_label.config(text="Timer")  # Reset the title label
    check_marks_label.config(text="")  # Reset the check marks
    reps = 0  # Reset the repetition counter

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer and manages the work/break cycle."""
    global reps
    reps += 1  # Increment the repetition counter

    work_sec = WORK_MIN * 60  # Calculate the work time in seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # Calculate the short break time in seconds
    long_break_sec = LONG_BREAK_MIN * 60  # Calculate the long break time in seconds

    if reps % 8 == 0:
        count_down(long_break_sec)  # Start the long break timer
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Start the short break timer
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)  # Start the work timer
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Counts down the timer and updates the UI."""
    global timer
    count_min = math.floor(count / 60)  # Calculate the minutes
    count_sec = count % 60  # Calculate the seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Add a leading zero if the seconds are single-digit

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Update the timer text
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Recursive call to decrement the timer
    else:
        start_timer()  # Start the next cycle
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"  # Add check marks for completed work sessions
        check_marks_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start and reset buttons
start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check marks label
check_marks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
check_marks_label.grid(column=1, row=3)

window.mainloop()