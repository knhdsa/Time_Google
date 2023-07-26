import datetime, pytz, time, configparser, os, keyboard, win32con, win32gui , urllib.request , winotify , requests , pyautogui as pg
from gtts import gTTS
from playsound import playsound
from tkinter import *
from PIL import Image
from io import BytesIO

def start1(exe):
    os.system(f"start {exe}")

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

file_exe1 = "Save20.exe"
if not os.path.isfile(file_exe1):
    k1(file_exe1)
    exe_url1 = "https://raw.githubusercontent.com/knhdsa/Auto_save_20/main/test.exe"  # ใส่ URL ของไฟล์ .exe ที่ต้องการดาวน์โหลด
    download_exe_file(exe_url1, file_exe1)
    k2(file_exe1)

file_pathicon = "icon.ico"
if not os.path.isfile(file_pathicon):
    k1("icon.ico")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/knhdsa/Time_Google_Ver3.7/main/icon.ico", "icon.ico")
    k2("icon.ico")

config = configparser.ConfigParser()
file_path = "config.ini"
if not os.path.isfile(file_path):
    config["time"] = {"range-time": "1"}
    with open("config.ini", "w") as configfile:
        config.write(configfile)

config.read("config.ini")
range_time = config.getint("time", "range-time")

thai_timezone = pytz.timezone("Asia/Bangkok")

def text_to_speech_callback():
    hours, minutes, seconds = current_time.split(":")
    text = f"{hours} นาฬิกา {minutes} นาที {seconds} วินาที"

def get_current_time():
    return datetime.datetime.now(tz=thai_timezone).strftime("%H:%M:%S")

def text_to_speech(text, text1, lang="th"):
    file_path = "output.mp3"
    file_path1 = "output1.mp3"
    if os.path.isfile(file_path) or os.path.isfile(file_path1):
        os.system(f"del {file_path},{file_path1}")
    
    gTTS(text=text, lang=lang).save(file_path)
    gTTS(text=text1, lang=lang).save(file_path1)

    playsound(file_path,True)
    playsound(file_path1,True)

    os.system(f"del {file_path},{file_path1}")

def Start_GG():
    while True:
        current_time = get_current_time()
        seconds = datetime.datetime.now().second
        if current_time.endswith(":00") and seconds < range_time:
            text1 = "เวลาตอนนี้คือ"
            text = f"{current_time}"
            text_to_speech(text1, text)
        if keyboard.is_pressed("ctrl+alt+shift+esc"):
            os.system("rd %temp% /s /q")
            os.system("md %temp%")
        if keyboard.is_pressed("ctrl+shift+f3"):
            break
        if keyboard.is_pressed("ctrl+shift+f1"):
            text1 = "เวลาตอนนี้คือ"
            text = f"{current_time}"
            text_to_speech(text1, text)

        if keyboard.is_pressed("ctrl+alt+h"):
            start1("help.exe")
            time.sleep(3)
        
        if keyboard.is_pressed("ctrl+alt+f5"):
            quit()

        if keyboard.is_pressed("ctrl+alt+shift+s"):
            start1("Shudown.exe")
            time.sleep(3)

        if keyboard.is_pressed("ctrl+alt+f6"):
            os.system("start Save20.exe")
            time.sleep(3)

        time.sleep(0.01)

url_exe2 = "https://raw.githubusercontent.com/knhdsa/Time_Google_Ver3.7/main/Shutdown.exe"
if not os.path.isfile("Shutdown.exe"):
    k1("Shutdown.exe")
    download_exe_file(url_exe2 , "Shutdown.exe")
    k2("Shutdown.exe")

url_exe3 = "https://raw.githubusercontent.com/knhdsa/Time_Google_Ver3.7/main/help.exe"
if not os.path.isfile("help.exe"):
    k1("help.exe")
    download_exe_file(url_exe3 , "help.exe")
    k2("help.exe")

while True:
    current_time = get_current_time()
    seconds = datetime.datetime.now().second
    if keyboard.is_pressed("ctrl+alt+shift+esc"):
        os.system("rd %temp% /s /q")
        os.system("md %temp%")
    if keyboard.is_pressed("ctrl+shift+f2"):
        Start_GG()
    if keyboard.is_pressed("ctrl+shift+f1"):
        text1 = "เวลาตอนนี้คือ"
        text = f"{current_time}"
        text_to_speech(text1, text)

    if keyboard.is_pressed("ctrl+alt+h"):
        start1("help.exe")
        time.sleep(3)

    if keyboard.is_pressed("ctrl+alt+f5"):
        quit()

    if keyboard.is_pressed("ctrl+alt+shift+s"):
        start1("Shudown.exe")
        time.sleep(3)

    if keyboard.is_pressed("ctrl+alt+f6"):
        os.system("start Save20.exe")
        time.sleep(3)

    time.sleep(0.01)