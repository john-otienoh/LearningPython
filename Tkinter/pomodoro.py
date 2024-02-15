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
LONG_BREAK_MIN = 20
timer = None
reps=0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    root.after_cancel(timer)
    canvas.itemconfig(canvas_text, text='00:00')
    timer_label.config(text='TIMER')
    check_label.config(text='')
    reps=0
    
#----------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Short Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text='Work Time', fg=GREEN)
 
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps/2)):
            marks += '>>'
        check_label.config(text=marks)  

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.config(bg=YELLOW, padx=50, pady=50)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
canvas_text = canvas.create_text(103, 112, text='00:00', fill='black', font=(FONT_NAME, 35, 'bold'))

timer_label = Label(text='TIMER', font=(FONT_NAME, 35),fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_btn = Button(text='Start', font=(FONT_NAME, 15, 'bold'), command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', font=(FONT_NAME, 15, 'bold'), command=reset_timer)
reset_btn.grid(column=2, row=2)

check_label = Label()
check_label.grid(column=1, row=3)
canvas.grid(column=1, row=1)
root.mainloop()