import datetime, pytz, time, configparser, os, keyboard, win32con, win32gui , urllib.request , winotify
from gtts import gTTS
from playsound import playsound
from tkinter import *
import pyautogui as pg
import requests
from PIL import Image
from io import BytesIO
from tkinter import messagebox

def k1(gx1):
    if not os.path.isfile(gx1):
        g1 = winotify.Notification(app_id="Time Google",
                                   title="กำลังโหลดโปรแกรมเพิ่ม",
                                   msg=f"โหลดโปรแกรม {gx1} อยู่")
        g1.show()

def k2(gx1):
    if os.path.isfile(gx1):
        g2 = winotify.Notification(app_id="Time Google",
                                   title="โหลดเสร็จแลัว",
                                   msg=f"โหลดโปรแกรม {gx1} เสร็จแลัว")

        g2.show()


def download_exe_file(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
    except Exception as e:
        root = Tk()
        root.title("Error 012")

        Label(root,text="Error 012",font=25).pack()

        root.mainloop()

file_gg = "Save20.exe"
if not os.path.isfile(file_gg):
    import urllib.request
    k1(file_gg)
    exe_url = "https://raw.githubusercontent.com/knhdsa/Auto_save_20/main/test.exe"  # ใส่ URL ของไฟล์ .exe ที่ต้องการดาวน์โหลด
    save_path = "Save20.exe"  # ตั้งตำแหน่งที่จะบันทึกไฟล์ .exe
    download_exe_file(exe_url, save_path)
    k2(file_gg)

def cancel_shutdown():
    os.system('shutdown /a')

# ดาวน์โหลดไฟล์ไอคอนจากออนไลน์และบันทึกไว้ในเครื่อง
k1("icon.ico")
urllib.request.urlretrieve('https://raw.githubusercontent.com/knhdsa/icon-Knhdsa/main/channels4_profile.ico', 'icon.ico')
k2("icon.ico")
def settime_shutown():
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

def help1():
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
    Label(root, text='4. ctrl+shift+f4 คือการซ้อนโปรแกรมทีเปิดค้างไว้', font=('Arial', 25), width=35).pack()
    Label(root, text='4. ctrl+alt+f4 คือการยกเลิกซ้อนโปรแกรมทีเปิดค้างไว้', font=('Arial', 25), width=35).pack()
    Label(root, text='5. ctrl+alt+shift+esc คือลบไฟล์ขยะ', font=('Arial', 25), width=35).pack()
    Label(root, text='6. ctrl+alt+h คือหน้านี้ที่เราดูสำสั่ง', font=('Arial', 25), width=35).pack()
    Label(root, text='7. ctrl+alt+f5 ปิดโปรแกรม', font=('Arial', 25), width=35).pack()
    Label(root, text='7. ctrl+alt+f6 เปิดระบบ save แบตเมื่อ 20% จะปิดคอมทันที', font=('Arial', 25), width=35).pack()

    root.mainloop()

config = configparser.ConfigParser()
file_path = "config.ini"
if not os.path.isfile(file_path):
    config['time'] = {'range-time': '1'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
config.read('config.ini')
range_time = config.getint('time', 'range-time')

thai_timezone = pytz.timezone('Asia/Bangkok')

def text_to_speech_callback():
    hours, minutes, seconds = current_time.split(":")
    text = f"{hours} นาฬิกา {minutes} นาที {seconds} วินาที"

def get_current_time():
    return datetime.datetime.now(tz=thai_timezone).strftime("%H:%M:%S")

def text_to_speech(text, text1, lang='th'):
    file_path = 'output.mp3'
    file_path1 = 'output1.mp3'
    if os.path.isfile(file_path) or os.path.isfile(file_path1):
        os.system(f'del {file_path},{file_path1}')
    
    gTTS(text=text, lang=lang).save(file_path)
    gTTS(text=text1, lang=lang).save(file_path1)

    playsound(file_path,True)
    playsound(file_path1,True)

    os.system(f'del {file_path},{file_path1}')

def run_in_background():
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

def run_no_background():
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_SHOW)

def k1():
    while True:
        current_time = get_current_time()
        seconds = datetime.datetime.now().second
        if current_time.endswith(':00') and seconds < range_time:
            text1 = 'เวลาตอนนี้คือ'
            text = f"{current_time}"
            text_to_speech(text1, text)
        if keyboard.is_pressed('ctrl+alt+shift+esc'):
            os.system('rd %temp% /s /q')
            os.system('md %temp%')
        if keyboard.is_pressed('ctrl+shift+f4'):
            run_in_background()
        if keyboard.is_pressed('ctrl+alt+f4'):
            run_no_background()
        if keyboard.is_pressed('ctrl+shift+f3'):
            break
        if keyboard.is_pressed('ctrl+shift+f1'):
            text1 = 'เวลาตอนนี้คือ'
            text = f"{current_time}"
            text_to_speech(text1, text)

        if keyboard.is_pressed('ctrl+alt+h'):
            help1()
        
        if keyboard.is_pressed('ctrl+alt+f5'):
            quit()

        if keyboard.is_pressed('ctrl+alt+shift+s'):
            settime_shutown()

        if keyboard.is_pressed("ctrl+alt+f6"):
            os.system("start Save20.exe")
            time.sleep(3)


        time.sleep(0.01)

while True:
    current_time = get_current_time()
    seconds = datetime.datetime.now().second
    if keyboard.is_pressed('ctrl+alt+shift+esc'):
        os.system('rd %temp% /s /q')
        os.system('md %temp%')
    if keyboard.is_pressed('ctrl+shift+f4'):
        run_in_background()
    if keyboard.is_pressed('ctrl+alt+f4'):
        run_no_background()
    if keyboard.is_pressed('ctrl+shift+f2'):
        k1()
    if keyboard.is_pressed('ctrl+shift+f1'):
        text1 = 'เวลาตอนนี้คือ'
        text = f"{current_time}"
        text_to_speech(text1, text)

    if keyboard.is_pressed('ctrl+alt+h'):
        help1()

    if keyboard.is_pressed('ctrl+alt+f5'):
        quit()

    if keyboard.is_pressed('ctrl+alt+shift+s'):
        settime_shutown()

    if keyboard.is_pressed("ctrl+alt+f6"):
        os.system("start Save20.exe")
        time.sleep(3)

    time.sleep(0.01)