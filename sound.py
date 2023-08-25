from gtts import gTTS
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import os
import threading

def k1():
    def text_to_speech():
        input_text = text_entry.get("1.0", "end-1c")
        if not input_text:
            messagebox.showwarning("Warning", "Please enter a text.")
            return
    
        output_dir = "C:/Users/nicha/Documents/sound_KH"
        os.makedirs(output_dir, exist_ok=True)
    
        output_audio_file = os.path.join(output_dir, "output_gtts.mp3")
    
        tts_thread = threading.Thread(target=convert_to_audio, args=(input_text, output_audio_file))
        tts_thread.start()
    
    def convert_to_audio(input_text, output_audio_file):
        tts = gTTS(text=input_text, lang='th')
        tts.save(output_audio_file)
        messagebox.showinfo("Success", f"Audio content saved as {output_audio_file}")
        play_thread = threading.Thread(target=play_audio, args=(output_audio_file,))
        play_thread.start()
    
    def play_audio(output_audio_file):
        playsound(output_audio_file)
    
    root = Tk()
    root.title("Text to Speech Converter")
    
    label = Label(root, text="Enter your text:", font=("Helvetica", 14))
    label.pack(pady=10)
    
    text_entry = Text(root, height=5, width=40, font=("Helvetica", 12))
    text_entry.pack()
    
    convert_button = Button(root, text="Convert to Speech", command=text_to_speech, font=("Helvetica", 14))
    convert_button.pack(pady=10)
    
    root.mainloop()
    