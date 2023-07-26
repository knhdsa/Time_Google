from tkinter import *
import psutil , winotify

def is_program_running(program_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == program_name:
            return True
    return False

# ตัวอย่างการใช้งาน
program_name = 'Time Google.exe'  # เปลี่ยนเป็นชื่อโปรแกรมที่คุณต้องการตรวจสอบ
if is_program_running(program_name):
    g1 = winotify.Notification(app_id="Time Google",
                                title=f"คุณได้เปิดโปรแกรม {program_name} นี้ไปแล้ว",
                                msg=f"คุณได้เปิดโปรแกรม {program_name} นี้ไปแล้ว")
    g1.show()
else:
    import codeall