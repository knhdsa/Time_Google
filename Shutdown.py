import os,win32con, win32gui
from tkinter import *

def settime_shutown():

    def cancel_shutdown():
        os.system('shutdown /a')
    
    def shutdown():
        hours = entry_hours.get()
        minutes = entry_minutes.get()
        seconds = entry_seconds.get()

        # ตรวจสอบว่าข้อมูลที่รับเข้ามาเป็นตัวเลขหรือไม่
        if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)

            total_seconds = (hours * 3600) + (minutes * 60) + seconds

            if total_seconds > 0:
                os.system(f'shutdown /s /t {total_seconds}')

    root = Tk()
    root.title('Auto Shutdown')
    root.configure(bg='green')

    # ตั้งค่าไอคอนให้กับหน้าต่าง
    root.iconbitmap('icon.ico')

    label_hours = Label(root, text="Hours:", font=("Arial", 15), bg='green')
    label_hours.pack()

    entry_hours = Entry(root, width=25, font=("Arial", 15))
    entry_hours.pack()

    label_minutes = Label(root, text="Minutes:", font=("Arial", 15), bg='green')
    label_minutes.pack()

    entry_minutes = Entry(root, width=25, font=("Arial", 15))
    entry_minutes.pack()

    label_seconds = Label(root, text="Seconds:", font=("Arial", 15), bg='green')
    label_seconds.pack()

    entry_seconds = Entry(root, width=25, font=("Arial", 15))
    entry_seconds.pack()

    btn_shutdown = Button(root, text="Shutdown", command=shutdown, width=25, font=("Arial", 15), bg='yellow')
    btn_shutdown.pack()

    btn_cancel_shutdown = Button(root, text="Cancel Shutdown", command=cancel_shutdown, width=25, font=("Arial", 15), bg='yellow')
    btn_cancel_shutdown.pack()

    root.mainloop()

    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MAXIMIZE)

settime_shutown()