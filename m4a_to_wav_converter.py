## gui based
import subprocess, ffmpeg
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_m4a_to_wav():
    input_files = filedialog.askopenfilenames(filetypes=[("M4A files", "*.m4a")])
    """
    convert m4a files into .WAV(PCM_S16LE, 48000Hz, mono).
    
    """
    if input_files:
        for input_file in input_files:
            output_file = os.path.splitext(input_file)[0] + '.wav'
            cmd = [
                'ffmpeg',
                '-i', input_file,
                '-acodec', 'pcm_s16le',
                '-ar', '48000',
                '-ac', '1',
                output_file
            ]
            try:
                subprocess.run(cmd, check=True)
                print(f"{output_file} convert successful.")
            except subprocess.CalledProcessError as e:
                tk.messagebox.showerror("error", f"error while converting {input_file}: {e}")
        tk.messagebox.showinfo("convert successful", "converting all selected files completed")
    
# GUI 생성
root = tk.Tk()
root.title("M4A to WAV converter")
button = tk.Button(root, text="select m4a files to convert", command=convert_m4a_to_wav)
button.pack(padx=20, pady=20)
root.mainloop()