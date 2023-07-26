import os , winotify
from tkinter import *

def windows1():
    def k1(gx1,gx2):
        g1 = winotify.Notification(app_id="Time Google",
                                    title=f"{gx1}",
                                    msg=f"{gx2}")
        g1.show()

    def shutdown():
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())

        total_seconds = (hours * 3600) + (minutes * 60) + seconds

        os.system(f'shutdown /s /t {total_seconds}')

        k1("จะได้ทำการปิดคอมในเวลา",f"{hours} Hours {minutes} นาที {seconds} วินาทีจะปิดคอมในเวลานี้")

    def cancel_shutdown():
        k1("ได้ทำการหยุดการปิดคอม","โปรแกรมได้ทำการหยุดการปิดคอม")
        os.system('shutdown /a')

    root = Tk()
    root.title('Auto Shutdown')
    root.configure(bg='green')

    # Set window icon
    # Note: Make sure 'icon.ico' exists in the current working directory or provide the correct path
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
