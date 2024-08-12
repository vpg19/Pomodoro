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
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def refresh():
    window.after_cancel(timer)
    global reps
    reps = 1
    timer_label.config(text='Timer',fg = GREEN)
    canvas.itemconfig(timer_text,text = '00:00')
    check.config(text = "")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    small_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in [1,3,5,7]:
        countdown(work_sec)
        timer_label.config(text='Work',fg = GREEN)
        reps += 1 
    elif reps in [2,4,6]:
        countdown(small_break_sec)
        timer_label.config(text='Break',fg = PINK)
        reps += 1
    elif reps == 8:
        countdown(long_break_sec)
        timer_label.config(text='Break',fg = RED)
        reps = 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx= 100,pady = 50,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='Code\\Pomodoro\\tomato.png')
canvas.create_image(100,112,image =tomato_img)
timer_text = canvas.create_text(110,130,text="00:00",font=(FONT_NAME,30,'bold'),fill='white')
canvas.grid(column=1,row=1)
timer_label = Label(text='Timer',font=(FONT_NAME,30,'bold'),bg=YELLOW,fg=GREEN)
timer_label.grid(column=1,row=0)
start = Button(text='Start',command=start_timer)
start.grid(column=0,row=2)
reset = Button(text='Reset',command = refresh)
reset.grid(column=2,row=2)
check = Label(fg=GREEN,bg=YELLOW,font=(25)) # type: ignore
check.grid(column=1,row=3)
window.mainloop()