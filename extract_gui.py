import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
import os

class AudioExtractorApp:
    def __init__(self, root):
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Mp4 to Mp3")
        self.root.configure(background='#add8e6')  
        self.file_path_var = tk.StringVar()
        self.file_path_label = tk.Label(self.root, textvariable=self.file_path_var, bg='#add8e6')
        self.file_path_label.pack()
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file, bg='#b3cde0')
        self.browse_button.pack()
        self.extract_button = tk.Button(self.root, text="Extract Audio", command=self.extract_audio, bg='#b3cde0')
        self.extract_button.pack()
        self.status_var = tk.StringVar()
        self.status_label = tk.Label(self.root, textvariable=self.status_var, bg='#add8e6')
        self.status_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        self.file_path_var.set(file_path)

    def extract_audio(self):
        if self.file_path_var.get():
            try:
                video = VideoFileClip(self.file_path_var.get())
                audio = video.audio
                audio_file_path = os.path.splitext(self.file_path_var.get())[0] + ".mp3"
                audio.write_audiofile(audio_file_path)
                self.status_var.set("Audio extracted successfully!")
            except Exception as e:
                self.status_var.set(f"An error occurred: {e}")
        else:
            self.status_var.set("Please select a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioExtractorApp(root)
    root.geometry("250x100")
    root.mainloop()
