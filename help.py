import requests , pyautogui as pg
from tkinter import *
from PIL import Image
from io import BytesIO

def start1():
    root = Tk()
    root.title('Help Command')

    icon_url = "https://raw.githubusercontent.com/knhdsa/icon-Knhdsa/main/channels4_profile.ico"  # URL ของไอคอนที่ต้องการโหลด
    response = requests.get(icon_url)
    icon_image = Image.open(BytesIO(response.content))

    # บันทึกไอคอนในรูปแบบไอคอน (.ico)
    icon_path = "icon.ico"
    icon_image.save(icon_path, format="ICO")

    # ตั้งค่าไอคอนของหน้าต่าง Tkinter
    root.iconbitmap(icon_path)

    Label(root, text='Help Command All', font=('Arial', 25)).pack()
    Label(root, text='1. ctrl+shift+f1 คือพูดเวลา', font=('Arial', 25), width=35).pack()
    Label(root, text='2. ctrl+shift+f2 คือพูดเวลาทุกนาทีที่เราตั้งในไฟล์ config.ini', font=('Arial', 25), width=40).pack()
    Label(root, text='3. ctrl+shift+f3 คือหยุดคำสั่งข้อ2', font=('Arial', 25), width=35).pack()
    Label(root, text='4. ctrl+alt+shift+esc คือลบไฟล์ขยะ', font=('Arial', 25), width=35).pack()
    Label(root, text='5. ctrl+alt+h คือหน้านี้ที่เราดูสำสั่ง', font=('Arial', 25), width=35).pack()
    Label(root, text='6. ctrl+alt+f5 ปิดโปรแกรม', font=('Arial', 25), width=35).pack()
    Label(root, text='7. ctrl+alt+f6 เปิดระบบ save แบตเมื่อ 20% จะปิดคอมทันที', font=('Arial', 25), width=35).pack()
    Label(root, text='8. ctrl+alt+shift+s คือตั้งเวลาปิดคอมถ้าไม่ได้ใส่เลขก็จะไม่ตั้ง' ,font=('Arial', 25), width=40).pack()
    Label(root, text='9. ctrl+alt+f7 แปลงข้อความเป็นเสียง' ,font=('Arial', 25), width=40).pack()

    root.mainloop()