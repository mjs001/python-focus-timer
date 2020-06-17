import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound

t_now = dt.datetime.now()
t_pom = 30*60
t_delta = dt.timedelta(0, t_pom)
t_fut = t_now + t_delta
delta_sec = 5*60
t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Focus Alarm started!", "\n It is now " +
                    t_now.strftime("%H:%M") + " hrs. \nTimer set for 30 minutes.")

total_pomo = 0
breaks = 0

while True:
    if t_now < t_fut:
        print('Focus!')
    elif t_fut <= t_now <= t_fin:
        print('in break')
        if breaks == 0:
            for i in range(5):
                winsound.Beep((i+100), 700)
            print('Break Time!')
            breaks += 1
    else:
        print('finished')
        breaks = 0
        for i in range(10):
            winsound.Beep((i+100), 500)
        usr_ans = messagebox.askyesno(
            "You have completed a cycle!", "Would you like to continue using the Focus Alarm?")
        total_pomo += 1
        if usr_ans == True:
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0, t_pom)
            t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)
            continue
        elif usr_ans == False:
            messagebox.showinfo(
                "Cycle has finished!", "\nYou have completed "+str(total_pomo)+" cycles today!")
        break
    print('sleeping')
    time.sleep(20)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")
